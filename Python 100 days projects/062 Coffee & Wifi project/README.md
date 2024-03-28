# Flask Café Wifi Project

A simple Flask web application to display a list of cafés with details like location, WiFi quality, power socket availability, and more. The application uses Flask and Bootstrap for styling, with café data stored in a CSV file.

## Features

- **Home Page**: Displays an introduction and a call to action to view the list of cafés.
- **Add Café**: A placeholder for a future feature to add new café entries through a form.
- **View Cafés**: Displays a list of cafés with details extracted from a CSV file, including links to Google Maps.

## Installation

Ensure you have Python 3.x installed on your machine.

1. **Clone the Repository**

```bash
git clone https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/062%20Coffee%20%26%20Wifi%20project
cd path-to-this-repo-at-your-pc
```
2. **Set up a Virtual Environment (Recommended)**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies and Run Application**
```bash
pip install Flask Flask-Bootstrap
python main.py
```

Access the web application at http://127.0.0.1:5000/.

## Application Structure
* main.py: Contains the Flask application, routes, and logic to read café data from the CSV file.
* templates/: Contains HTML templates for rendering the website. It includes base.html for the base layout, index.html for the home page, and cafes.html for displaying the list of cafés.
* static/: This directory should contain static files like CSS stylesheets. You'll need to create this directory and add any required static files.

## Routes
* /: The home page with a welcome message and a button to view cafés.
* /add: A placeholder route for a future page where users can add new cafés.
* /cafes: Displays a table of cafés with details like name, location, WiFi quality, and more, pulled from a CSV file.