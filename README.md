Building a Secure Web Application
Detection and Mitigation of Security Vulnerabilities
This project is a Flask-based web application developed for the CSC429 course project. The objective of the project is to demonstrate common web security vulnerabilities and how they can be mitigated using secure coding practices.
The application includes two versions:

Vulnerable Version
Demonstrates common web vulnerabilities for testing and educational purposes.
Secure Version
Implements security mechanisms to mitigate vulnerabilities and protect the application.

The application includes:

User Registration
User Login
Dashboard
Comments Page
Admin Page
Session Management

Technologies Used

Python
Flask
SQLite
Bootstrap 5
bcrypt
HTML/CSS
Jinja2

Application Versions
1. Vulnerable Version
The vulnerable version demonstrates several security weaknesses, including:
SQL Injection
Unsafe SQL query construction allows attackers to manipulate database queries.
Weak Password Storage
Passwords may be stored insecurely without proper hashing.
Cross-Site Scripting (XSS)
User input may be rendered unsafely, allowing malicious JavaScript execution.
Broken Access Control
Unauthorized users may attempt to access restricted pages directly.
Weak Session and Communication Security
Insufficient session protection and lack of encrypted communication may expose sensitive information.
2. Secure Version
The secure version mitigates vulnerabilities using secure development techniques.
SQL Injection Prevention
Parameterized queries are used instead of unsafe SQL string formatting.
Secure Password Storage
Passwords are hashed using bcrypt before being stored in the database.
XSS Prevention
Jinja2 automatic escaping is used to safely render user input.
Role-Based Access Control (RBAC)
Only authorized users with the admin role can access the admin page.
Session Security
Secure session cookie settings are configured to improve session protection.
HTTPS/TLS Recommendation
HTTPS/TLS is recommended in production environments to encrypt transmitted data.
Project Structure
The project folder is organized as follows:
security-project-main/
│
├── app.py                  # Secure version Flask application
├── vulnerable.py           # Vulnerable version Flask application
├── cert.pem                # SSL certificate (for HTTPS)
├── key.pem                 # SSL private key (for HTTPS)
├── README.md               # Project documentation
│
├── users.db                # Database for the secure version (auto-generated)
├── vulnerable.db           # Database for the vulnerable version (auto-generated)
│
└── templates/              # HTML templates for the secure version
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── comments.html
│   └── admin.html
│
└── vulnerablecode/         # HTML templates for the vulnerable version
    ├── logincopy.html
    ├── registercopy.html
    ├── dashboardcopy.html
    ├── commentscopy.html
    └── admincopy.html

Note: Each version uses its own separate database:

users.db is used by the secure version (app.py)
vulnerable.db is used by the vulnerable version (vulnerable.py)

Both databases are automatically created when the respective script is run for the first time.

File / FolderDescriptionapp.pySecure Flask applicationvulnerable.pyVulnerable Flask applicationtemplates/HTML templates for the secure versionvulnerablecode/HTML templates for the vulnerable versionusers.dbSQLite database for the secure versionvulnerable.dbSQLite database for the vulnerable versioncert.pemSSL certificatekey.pemSSL private keyREADME.mdProject documentation
Application Setup & Database
Automatic Initialization: The database is automatically generated the moment the script is executed for the first time. The init_db() function checks if the required tables (users and comments) exist and creates them if they are missing, ensuring the application is ready for immediate use.
User Roles & Access Control

Role Assignment: By default, every new account registered through the /register page is assigned the role of 'user'.
Admin Access: To grant administrative privileges, the role must be manually updated to 'admin' directly within the database using the SQLite Explorer extension in VS Code. This manual process acts as an additional security measure, ensuring no unauthorized user can elevate their own permissions through the web interface.

Steps to Run the Application:
1. Open the Project Folder
Open the project folder using Visual Studio Code.
2. Install Required Libraries
Run the following command in the terminal:
bashpip install flask bcrypt

3. Run the Application
The application consists of two versions. Since Flask specifically requires a folder named templates to render HTML pages, you must ensure the correct folder is renamed before running the script.
A. To run the Vulnerable Version:

Rename the folder vulnerablecode to templates.
Run the vulnerable script:

bashpython vulnerable.py
B. To run the Secure Version:

For the secure version, use the main folder named templates that we have provided in the project files.
If you previously renamed the vulnerable folder to templates, make sure to change its name first to avoid conflicts.
Before running the secure version, you need to generate SSL certificate files (cert.pem and key.pem) to enable HTTPS. Follow these steps:

Download and install Git from https://git-scm.com/
Right-click on the project folder and select "Git Bash Here"
Run the following command in the Git Bash terminal:



bashMSYS_NO_PATHCONV=1 openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "//CN=localhost"

This will generate cert.pem and key.pem in the project folder, which are required for HTTPS.


Run the secure script:

bashpython app.py

4. Open the Application
For the vulnerable version, open the browser and go to:
texthttp://127.0.0.1:5000
For the secure version, open the browser and go to:
texthttps://127.0.0.1:5001

Note: Since a self-signed certificate is used, the browser may show a security warning. Click "Advanced" and then "Proceed" to continue.


Application Pages
PageDescription/registerCreate a new account/loginUser login page/dashboardUser dashboard/commentsComments page for XSS testing/adminProtected admin page

Security Features Implemented
Security FeatureDescriptionSQL Injection PreventionPrevents malicious SQL manipulation using parameterized queriesbcrypt Password HashingProtects passwords by storing hashed valuesXSS ProtectionPrevents JavaScript execution from user inputRBACRestricts admin page access to authorized users onlySession SecurityProtects session cookies and login sessions

Security Testing Instructions
Each vulnerability can be tested in both the vulnerable and secure versions.

1. SQL Injection Test
Vulnerable Input
Username:
text' OR 1=1 --
Password:
textanything
Expected Result in Vulnerable Version
The login may succeed without knowing the correct password.
Expected Result in Secure Version
The login fails because parameterized queries are used.

2. Weak Password Storage Test

Register a new user.
Open users.db using the SQLite extension in VS Code.
Check the password column.

Expected Result in Vulnerable Version
Passwords may appear as plain text.
Expected Result in Secure Version
Passwords appear as bcrypt hashes starting with:
text$2b$

3. XSS Test
Test Input
html<script>alert('XSS')</script>
Steps

Login to the application.
Open the comments page.
Submit the payload above.

Expected Result in Vulnerable Version
A popup alert appears because the script executes.
Expected Result in Secure Version
The script is displayed as plain text and does not execute.

4. Access Control Test
Steps

Login using a normal user account.
Open:

text/admin
Expected Result in Vulnerable Version
Unauthorized users may access the admin page.
Expected Result in Secure Version
The system displays:
textAccess denied. Admins only.

Challenges Faced

Understanding secure password hashing using bcrypt
Preventing SQL Injection using parameterized queries
Implementing XSS protection using Jinja2 escaping
Restricting unauthorized access using RBAC
Testing vulnerable and secure versions separately


Future Improvements

Implement Rate Limiting
Improve password complexity validation
Add logging and monitoring features
Implement multi-factor authentication (MFA)


Resources

Flask Documentation
https://flask.palletsprojects.com/
Bootstrap Documentation
https://getbootstrap.com/
bcrypt Documentation
https://pypi.org/project/bcrypt/
SQLite Documentation
https://www.sqlite.org/


GitHub Repository
