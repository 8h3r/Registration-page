# Registration-page

This is a Python project that implements a login and registration system using MySQL database and the CustomTkinter library for the graphical user interface (GUI). The project has two main components: the login page and the registration page.
Login Page.
The login page allows existing users to enter their username and password to authenticate and access the main window. Upon successful login, an animated welcome message is displayed with the user's nickname. The login page also includes a button to navigate to the registration page for new users.
Registration Page.
The registration page allows new users to sign up by providing their username, email, nickname, phone number, and password. The input fields are validated to ensure the data meets certain requirements (e.g., username length, email format, password strength). If the input is valid, the user's information is inserted into the MySQL database, and a success message is displayed.

Features:
User-friendly GUI with CustomTkinter library
Input validation for registration fields
Error message display for invalid input
Animated welcome message on successful login
MySQL database integration for storing user information
Window blur effect using the BlurWindow library

Requirements:
Python
CustomTkinter library
MySQL server
MySQL Connector/Python

Usage:
Set up a MySQL server and create a database named "Personal" with a table named "Login_info" containing columns for username, email, nickname, phoneno, and password.
Install the required Python libraries (customtkinter, mysql-connector-python, BlurWindow).
Update the MySQL connection details in the code with your MySQL server credentials.
Run the Python script, and the login and registration GUI will be displayed.

Note.
This project is a basic implementation and may require additional features and improvements for production-ready use, such as secure password storage, session management, and input sanitization.
