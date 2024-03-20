# Cafe API Project
## Overview
This project is focused on practicing the construction of APIs using Flask, a popular micro web framework written in Python. The Cafe API allows for the creation, retrieval, updating, and deletion of cafe records in a database. It is designed as a learning tool for understanding how web APIs work and how they interact with a database using SQLAlchemy.

## Features
* Add New Cafe: Allows users to add a new cafe record to the database.
* List All Cafes: Retrieves a list of all cafes from the database.
* Get Random Cafe: Fetches a random cafe record.
* Search Cafe by Location: Enables searching for cafes in a specific location.
* Update Cafe Price: Allows for updating the coffee price of a specific cafe.
* Delete Cafe: Enables the deletion of a cafe record from the database, given the correct API key.

## Installation
1. Clone the repository to your local machine.

2. Install the required packages using the following commands:

On Windows:
```
python -m pip install -r requirements.txt
```

On MacOS:
```
pip3 install -r requirements.txt
```
This will install all the necessary packages listed in requirements.txt.

#### How to Run
1. Navigate to the project directory in your terminal.
2. un the Flask application with the command:

```
python -m flask run
```

3. The server will start, and you can access the API at localhost:5000 by default.


#### API Endpoints

- **GET `/random`**: Fetch a random cafe.
- **GET `/all`**: List all cafes.
- **GET `/search?loc=<location>`**: Search for cafes by location.
- **POST `/add`**: Add a new cafe. Required fields: `name`, `map_url`, `img_url`, `location`, `seats`, `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, `coffee_price`.
- **PATCH `/update-price/<int:cafe_id>?new_price=<new_price>`**: Update the price of coffee for a specific cafe.
- **DELETE `/report-closed/<int:cafe_id>?api-key=<api_key>`**: Delete a cafe if the correct API key is provided.

#### Technologies Used

- Flask for creating the web server and handling API requests.
- SQLAlchemy for database interaction.
- SQLite for the database engine.

#### Note

This project is intended for educational purposes to understand the basics of API development, database integration, and web server management using Python and Flask.