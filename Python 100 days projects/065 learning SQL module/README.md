# Projet 65: SQLAlchemy and SQLite Learning Repository

This repository is designed for learning and experimenting with SQLAlchemy alongside SQLite through Python. It includes practical examples to understand database operations using Flask, SQLAlchemy ORM, and direct SQLite3 connections. Ideal for beginners looking to get hands-on with Python-based database management.

## Installation

To get started, clone this repository to your local machine:

```
git clone https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/065%20learning%20SQL%20module
```

Ensure you have Python installed. Then, install the required dependencies:

```
pip install flask sqlalchemy
```

## Project Structure

- **learningSQL.py**: Introduces basic database operations with SQLite3. It demonstrates how to create a database, define a table, and insert records directly using SQLite3 commands.

- **learningSQL2.py** & **learningSQL3.py**: Expand on the initial script by integrating Flask and SQLAlchemy ORM for database interactions. These files cover creating models, adding records, querying, updating, and deleting data through the ORM layer.

## Key Concepts Covered

- **Database Connection**: Establishing connections to SQLite databases using both SQLite3 and SQLAlchemy ORM.
- **Model Definition**: Using SQLAlchemy ORM to define database models.
- **CRUD Operations**: Demonstrating Create, Read, Update, and Delete (CRUD) operations on a `Book` table.
- **Flask Integration**: Configuring Flask to work with SQLAlchemy for web-based database interactions.

## Running the Examples

To run any of the scripts:

```
python learningSQL.py
python learningSQL2.py
python learningSQL3.py
```

Ensure you activate the virtual environment if you're using one.

## Learning Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
- [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this learning project.

## License

This project is open source and available under the [MIT License](LICENSE).
