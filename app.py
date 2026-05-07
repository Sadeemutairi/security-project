from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt
import os

app = Flask(__name__)

# -------- BEFORE (Vulnerable) --------
# A weak and hardcoded secret key was used
# Session cookies were not securely configured

# app.secret_key = "key123"


# -------- AFTER (Fixed) --------
# A strong random secret key is used
# Session cookies are configured with secure settings

app.secret_key = os.urandom(24)

app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
# Use True only when running with HTTPS
app.config["SESSION_COOKIE_SECURE"] = True


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

    conn.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
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

        # ------------- 2. Weak Password Storage (hashing) -------------
        
        # ------------- Weak Password Storage (BEFORE fix): -------------
        # Passwords were stored in plain text without encryption
        # password = request.form["password"]

        
        # ------------- Secure Password Storage code (AFTER fix): -------------
        # Passwords are hashed using bcrypt
        password = request.form["password"].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()) 

        conn = get_db()
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hashed_password, "user")
        )

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

        # ------------- 1. SQL Injection -------------

        # ------------- SQL Injection Vulnerable code (BEFORE fix):-------------
        # SQL Injection input Username: ' OR 1=1 --
        # This input makes the condition always true
        # The attacker can login without knowing the password

        # query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        # print("QUERY:", query)
        # user = conn.execute(query).fetchone()

        # ------------- SQL Injection Secure code (AFTER fix): -------------
        # Parameterized queries are used to prevent SQL Injection
        # The system retrieves the user by username only
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()


        # ------------- Secure Password Verification -------------
        # Instead of checking the password in SQL
        # The entered password is compared with the stored hashed password
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]): # compare the entered password with the hashed one stored in DB
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
    

# ------------- 3. Cross-Site Scripting (XSS)-------------

# ------------- XSS  Vulnerable code (BEFORE fix): -------------
# User input is stored and displayed without sanitization.
# If the template uses the 'safe' filter, it allows execution of malicious scripts
# Example attack: <script>alert('XSS')</script>

# ------------- XSS  Vulnerable code (AFTER fix): -------------
# Input is rendered safely using Jinja2 default escaping
# The 'safe' filter is removed from the template to prevent script execution
@app.route("/comments", methods=["GET", "POST"])
def comments():
    if "username" not in session:
        return redirect("/login")

    if request.method == "POST":
        comment = request.form["comment"]

        conn = get_db()
        conn.execute(
            "INSERT INTO comments (text) VALUES (?)",
            (comment,)
        )
        conn.commit()
        conn.close()

    conn = get_db()
    comments = conn.execute("SELECT * FROM comments").fetchall()
    conn.close()

    return render_template("comments.html", comments=comments)


@app.route("/admin")
def admin():
    if "username" not in session:
        return redirect("/login")

    # ------------- 4. Access Control -------------

    # ------------- Access Control Vulnerable code (BEFORE fix): -------------
    # No role check is performed — any logged-in user can access the admin page
    # return render_template("admin.html")

    # ------------- Access Control Secure code (AFTER fix): -------------
    # Role-based access control (RBAC) is enforced
    # Only users with the 'admin' role are allowed to proceed
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (session["username"],)
    ).fetchone()
    conn.close()

    if user["role"] != "admin":
        return "Access denied. Admins only."

    return render_template("admin.html")


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# Run app
if __name__ == "__main__":
    init_db()
    # Change 5000 to 5001
    app.run(debug=True, port=5001, ssl_context=('cert.pem', 'key.pem'))  # self-signed cert (SSL)
