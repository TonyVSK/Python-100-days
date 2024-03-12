from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlite3

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


# ==============================================================================================================
# BASIC 
app = Flask(__name__)

all_books = []



class Base(DeclarativeBase):
  pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-others-new-books-collection.db"



db = SQLAlchemy(model_class=Base)

db.init_app(app)

# ==============================================================================================================
# CREATING BOOK TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# ==============================================================================================================
# FLASK PAGE DEFINITIONS
@app.route('/')
def home():
    # Getting books from database
    with app.app_context():
        result = db.session.query(Book).all()  # Search all books
        books = [{"title": book.title, "author": book.author, "rating": book.rating} for book in result]

    # Renderizing template with books
    return render_template("index.html", books=books)


counting = 0
@app.route("/add", methods=["GET", "POST"])
def add():
    global counting
    counting += 1
    if request.method=="POST":
        information = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(information)
        # ==============================================================================================================
        # CREATING RECORD
        try:
            with app.app_context():
                new_book = Book(title=information["title"], author=information["author"], rating=information["rating"])
                db.session.add(new_book)
                db.session.commit()
        except Exception:
            pass
        # ==============================================================================================================


        return redirect(url_for('home'))       
    return render_template("add.html")




if __name__ == "__main__":
    app.run(debug=True)