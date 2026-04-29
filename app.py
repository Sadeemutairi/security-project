from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "key123"

# Connect to database
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT DEFAULT 'user'
        )
    """)
    conn.commit()
    conn.close()

# Home → redirect to login
@app.route("/")
def home():
    return redirect("/login")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        
        # Weak Password Storage (before fix):
        # Passwords were stored in plain text without encryption
        # password = request.form["password"]

        # Secure Password Storage (after fix):
        # Passwords are hashed using bcrypt
        password = request.form["password"].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())


        conn = get_db()
        conn.execute(
           "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hashed_password, "user")
        )

        #conn.execute(
            #"INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            #(username, password, "user")
        #)

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        
        # ------------- SQL Injection Vulnerable code: -------------
        # SQL Injection input Username: ' OR 1=1 --
        # This input makes the condition always true
        # The attacker can login without knowing the password

        #query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        #print("QUERY:", query)
        #user = conn.execute(query).fetchone()

        # ------------- End SQL Injection Vulnerable code -------------
        
        #user = conn.execute(
            #"SELECT * FROM users WHERE username=? AND password=?",
            #(username, password)

        
        # ------------- SQL Injection Secure code: -------------  
        # Previously, the query checked both username and password in SQL
        # The system retrieves the user by username only
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()



        # Secure Password Verification
        # Instead of checking the password in SQL
        # The entered password is compared with the stored hashed password
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            session["username"] = user["username"]
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (session["username"],)
    ).fetchone()
    return render_template("dashboard.html", user=user)

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# Run app
if __name__ == "__main__":
    init_db()
    app.run(debug=True)