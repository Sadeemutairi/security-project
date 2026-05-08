# Building a Secure Web Application
## Detection and Mitigation of Security Vulnerabilities

This project is a Flask-based web application developed for the CSC429 course project. The objective of the project is to demonstrate common web security vulnerabilities and how they can be mitigated using secure coding practices.

The application includes two versions:

1. Vulnerable Version  
   Demonstrates common web vulnerabilities for testing and educational purposes.

2. Secure Version  
   Implements security mechanisms to mitigate vulnerabilities and protect the application.

The application includes:
- User Registration
- User Login
- Dashboard
- Comments Page
- Admin Page
- Session Management

# Technologies Used

- Python
- Flask
- SQLite
- Bootstrap 5
- bcrypt
- HTML/CSS
- Jinja2


# Application Versions

## 1. Vulnerable Version

The vulnerable version demonstrates several security weaknesses, including:

### SQL Injection
Unsafe SQL query construction allows attackers to manipulate database queries.

### Weak Password Storage
Passwords may be stored insecurely without proper hashing.

### Cross-Site Scripting (XSS)
User input may be rendered unsafely, allowing malicious JavaScript execution.

### Broken Access Control
Unauthorized users may attempt to access restricted pages directly.

### Weak Session and Communication Security
Insufficient session protection and lack of encrypted communication may expose sensitive information.

## 2. Secure Version

The secure version mitigates vulnerabilities using secure development techniques.

### SQL Injection Prevention
Parameterized queries are used instead of unsafe SQL string formatting.

### Secure Password Storage
Passwords are hashed using bcrypt before being stored in the database.

### XSS Prevention
Jinja2 automatic escaping is used to safely render user input.

### Role-Based Access Control (RBAC)
Only authorized users with the admin role can access the admin page.

### Session Security
Secure session cookie settings are configured to improve session protection.

### HTTPS/TLS Recommendation
HTTPS/TLS is recommended in production environments to encrypt transmitted data.

# Project Structure

| File / Folder | Description |
|---|---|
| `app.py` | Main Flask application |
| `templates/` | HTML templates |
| `login.html` | Login page |
| `register.html` | Registration page |
| `dashboard.html` | User dashboard |
| `comments.html` | Comments page used for XSS testing |
| `admin.html` | Admin page protected by RBAC |
| `users.db` | SQLite database |
| `README.md` | Project documentation |


# Application Setup & Database
**Automatic Initialization:** The database `users.db` is automatically generated the moment the `app.py` script is executed for the first time. The `init_db()` function checks if the required tables (users and comments) exist and creates them if they are missing, ensuring the application is ready for immediate use.

## User Roles & Access Control
* **Role Assignment:** By default, every new account registered through the `/register` page is assigned the role of **'user'**. 
* **Admin Access:** To grant administrative privileges, the role must be manually updated to **'admin'** directly within the database (e.g., using DB Browser for SQLite). This manual process acts as an additional security measure, ensuring no unauthorized user can elevate their own permissions through the web interface.

## Steps to Run the Application:
## 1. Open the Project Folder

Open the project folder using Visual Studio Code.

## 2. Install Required Libraries

Run the following command in the terminal:

```bash
pip install flask bcrypt
```

---

## 3. Run the Application

```bash
python app.py
```

---

## 4. Open the Application

Open the browser and go to:

```text
http://127.0.0.1:5000
```

---

# Application Pages

| Page | Description |
|---|---|
| `/register` | Create a new account |
| `/login` | User login page |
| `/dashboard` | User dashboard |
| `/comments` | Comments page for XSS testing |
| `/admin` | Protected admin page |

---

# Security Features Implemented

| Security Feature | Description |
|---|---|
| SQL Injection Prevention | Prevents malicious SQL manipulation using parameterized queries |
| bcrypt Password Hashing | Protects passwords by storing hashed values |
| XSS Protection | Prevents JavaScript execution from user input |
| RBAC | Restricts admin page access to authorized users only |
| Session Security | Protects session cookies and login sessions |

---

# Security Testing Instructions

Each vulnerability can be tested in both the vulnerable and secure versions.

---

# 1. SQL Injection Test

## Vulnerable Input

Username:
```text
' OR 1=1 --
```

Password:
```text
anything
```

## Expected Result in Vulnerable Version
The login may succeed without knowing the correct password.

## Expected Result in Secure Version
The login fails because parameterized queries are used.

---

# 2. Weak Password Storage Test

1. Register a new user.
2. Open `users.db` using the SQLite extension in VS Code.
3. Check the password column.

## Expected Result in Vulnerable Version
Passwords may appear as plain text.

## Expected Result in Secure Version
Passwords appear as bcrypt hashes starting with:

```text
$2b$
```

---

# 3. XSS Test

## Test Input

```html
<script>alert('XSS')</script>
```

## Steps
1. Login to the application.
2. Open the comments page.
3. Submit the payload above.

## Expected Result in Vulnerable Version
A popup alert appears because the script executes.

## Expected Result in Secure Version
The script is displayed as plain text and does not execute.

---

# 4. Access Control Test

## Steps
1. Login using a normal user account.
2. Open:

```text
/admin
```

## Expected Result in Vulnerable Version
Unauthorized users may access the admin page.

## Expected Result in Secure Version
The system displays:

```text
Access denied. Admins only.
```

---

# Challenges Faced

- Understanding secure password hashing using bcrypt
- Preventing SQL Injection using parameterized queries
- Implementing XSS protection using Jinja2 escaping
- Restricting unauthorized access using RBAC
- Testing vulnerable and secure versions separately

---

# Future Improvements

- Enable HTTPS in deployment environments
- Improve password complexity validation
- Add logging and monitoring features
- Implement multi-factor authentication (MFA)

---

# Resources

- Flask Documentation  
  https://flask.palletsprojects.com/

- Bootstrap Documentation  
  https://getbootstrap.com/

- bcrypt Documentation  
  https://pypi.org/project/bcrypt/

- SQLite Documentation  
  https://www.sqlite.org/

---

# GitHub Repository

........
