# Secure Web Application - Detection and Mitigation of Vulnerabilities
Flask-based web application designed to demonstrate the detection and mitigation of common security vulnerabilities. The application includes a user management system with registration, login, and a dashboard, along with a secure comment system.
# Steps to run the Application:
1. Open the project folder in VS Code.
2. Install the required libraries:
   pip install flask bcrypt
3. Run the application:
   python app.py
4. Open the browser and go to the provided link
   
5. Register a new user, then log in to access the dashboard.
# Instructions to test security features:
SQL Injection Test:
1. Go to the login page.
2. In the vulnerable version, enter:
   Username: ' OR 1=1 --
   Password: anything
3. This should allow login without knowing the password.
4. In the fixed version, the same input should fail because parameterized queries are used.

Weak Password Storage Test:
1. Register a new user.
2. Open users.db using the SQLite extension in VS Code.
3. Check the password column.
4. The password should appear as a bcrypt hash starting with $2b$, not as plain text.
