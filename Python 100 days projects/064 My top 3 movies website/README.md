# My Top 3 Movies

## Project Overview

This project is a web application that allows users to maintain a list of top 3 favorite movies. The application provides functionalities to add, delete, and update movie details. It's built with Flask, a micro web framework written in Python, and uses Flask-Bootstrap for styling, Flask-WTF for form handling, and Flask-SQLAlchemy for database interactions.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
- **Flask-Bootstrap**: An extension for Flask that integrates Bootstrap front-end framework with the Flask application.
- **Flask-WTF**: An extension for Flask that adds integration with WTForms, a flexible forms validation and rendering library for Python web development.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, a SQL toolkit and ORM for Python.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) library that gives application developers the full power and flexibility of SQL.
- **SQLite**: A C library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.

## Installation

To set up the project on your local machine:

1. Clone the repository to your local machine:
   ```
   https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/064%20My%20top%2010%20movies%20website
   ```
   
2. Navigate to the project directory:
   ```
   cd my-top-3-movies
   ```

3. Install de required packages:
    ```
    pip install -r requirements.txt
    ```

## Running the Application
To start the Flask server, run:
```
flask run
```
Or you can use:
```
python -m flask run
```
Access the application in your web browser at http://localhost:5000.

## Project Structure
- **main.py**: The entry point to the Flask application. This script runs the Flask server and contains the route definitions.
- **models.py**: Contains the SQLAlchemy models for the Movie database table.
- **templates/**: This directory holds the HTML templates for the application, using Jinja2 templating language.
- **static/**: Contains static files like CSS and JavaScript files used by the application.
- **requirements.txt**: A text file listing the projects dependencies, which can be installed using pip.

## Features
* Add a new movie to the list.
* View the list of top 10 movies.
* Update movie details.
* Delete a movie from the list.

## License
This project is open-source and available under the MIT License.