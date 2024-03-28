# Virtual Bookshelf

This application is a simple Flask web application designed for managing a book collection. It allows users to view a list of books, add new books to the collection, and stores book details such as title, author, and rating in a SQLite database. This application uses Flask and SQLAlchemy for the backend, with simple HTML forms for user interaction.

## Features

- **View Books**: Displays a list of all books in the collection on the homepage.
- **Add Books**: Users can add new books to the collection through a form submission.

## Installation and Start

To run this project locally, you'll need Python and pip installed on your system.

1. **Clone the repository**:

```bash
git clone https://github.com/TonyVSK/Python-100-days/tree/main/Python%20100%20days%20projects/063%20databases%20SQL%20-%20virtual%20bookshelf
cd path-to-this-repo-at-your-pc
```

2. **Set up a virtual environment** (optional but recommended):
```
python -m venv venv
venv\Scripts\activate
```

3. **Install the required packages**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python main.py
```
The application will start on http://127.0.0.1:5000/.

## Application Structure
**Database Setup**: Uses SQLAlchemy with SQLite to manage book records. The Book model represents the schema for book information stored in the database.

**Flask Application**: The main application setup is in main.py, defining routes for viewing and adding books.

## Routes
* /: The homepage displays all books in the collection. Book details include title, author, and rating.
* /add: A form to add a new book to the collection. Submits to the same URL and redirects to the homepage upon success.

## How to Use
**Viewing the Book Collection**: Simply navigate to the homepage to see a list of all books in the collection.
**Adding a New Book**: Click on the link or navigate to /add to access the form for adding a new book. Fill in the details and submit.