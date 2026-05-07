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


# How to Run the Application

## 1. Open the Project Folder

Open the project folder using Visual Studio Code.

## 2. Install Required Libraries

Run the following command in the terminal:
```bash
pip install flask bcrypt
