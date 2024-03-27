# Hash and Salt Passwords Tutorial

This project is designed as an educational resource to demonstrate the implementation of hash and salt techniques for securing passwords. Utilizing Flask, SQLAlchemy, and Flask-Login, it offers a practical example of user authentication and security in web applications.

## Features

- **User Registration and Authentication**: Securely manage user sign-ups and logins.
- **Password Hashing**: Utilize `werkzeug.security` to hash passwords.
- **Salt Generation**: Automatically generate salts to add an extra layer of security.
- **User Session Management**: Handle user sessions with Flask-Login.

## Getting Started

### Prerequisites

Ensure you have Python and Flask installed on your system. If not, you can download them from [Python's official site](https://www.python.org/downloads/) and follow the instructions to install Flask using pip:

```
pip install Flask
```

### Installation
1. Clone the repository to your local machine:
```
https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/068%20authentication%20with%20flask
```
2. Install the required packages:
```
pip install -r requirements.txt
```

### Running the Application
1. Set the Flask application variable:
On Unix/Linux/Mac:
```
export FLASK_APP=app.py
```
On Windows:
```
set FLASK_APP=app.py
```

2. Run the Flask application:
```
flask run
```
Open a web browser and navigate to http://127.0.0.1:5000/ to access the application.


## Understanding the Code
-**Password Hashing and Salting**: The generate_password_hash function from werkzeug.security is used to hash passwords with a salt. This method ensures that even if two users have the same password, their stored passwords will be different due to the salt.

-**User Authentication**: Flask-Login is utilized for managing user sessions. It requires the implementation of a user loader callback, which is used to reload the user object from the user ID stored in the session.

-**Database Setup**: SQLAlchemy is used for database interactions. A User model is defined with fields for storing user information, including the hashed password.


## Contributing
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.