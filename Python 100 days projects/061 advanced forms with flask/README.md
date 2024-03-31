# Advanced Forms with Flask: Flask Login Form with Validation and Bootstrap

This project is a Flask application that demonstrates the use of Flask-WTF for form handling with validation and Flask-Bootstrap for styling. It includes a login form that validates user input against predefined criteria and showcases different templates based on the validation result.

## Features

- **Flask-WTF Form Handling**: Utilizes Flask-WTF for secure and easy form rendering, data validation, and CSRF protection.
- **Email and Password Validation**: Validates the email with specific conditions and ensures the password meets length requirements.
- **Flask-Bootstrap Integration**: Uses Flask-Bootstrap to apply Bootstrap 5 styling to the Flask application, making it responsive and aesthetically pleasing.
- **Conditional Template Rendering**: Renders different templates based on the success or failure of form submission and validation.

## Installation

To run this project, ensure you have Python and pip installed. Follow these steps:

1. **Clone the Repository**:
```bash
git clone https://your-repository-link-here.git
```

2. **Navigate to the Project Directory**:
```bash
cd path-to-your-project
```

3. **Install Dependencies**:
Install Flask, Flask-WTF, WTForms, and Flask-Bootstrap with pip:
```bash
pip install flask flask-wtf wtforms flask-bootstrap
```

## Configuration

- **Secret Key**: The application requires a secret key to protect web forms against Cross-Site Request Forgery (CSRF). Define your secret key in the app configuration:
```python
app.secret_key = "your-secret-key-here"
```

- **Form Class**: Customize the LoginForm class in main.py to change validation rules or add new fields.

## Running the Application
Launch the application using Flask:
```bash
flask run
```
Or directly through Python:
```bash
python main.py
```
By default, the application will be available at http://127.0.0.1:5000/.

## Usage
- **Homepage**: Access the homepage by navigating to /. It's a simple placeholder for the login functionality.
- **Login Page**: The login form can be accessed at /login. It includes fields for email and password. The form validates:
    * Email must be admin@email.com.
    * Password must be at least 8 characters long.
- **Success or Denied Page**: Depending on the validation outcome, users are redirected to either a success or denied page.

## Support
For support, open an issue on the GitHub repository.

## Contributions
Your contributions are welcome! Please fork the repository, make your changes, and submit a pull request.