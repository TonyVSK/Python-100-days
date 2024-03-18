from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlite3



# ==============================================================================================================
# BASIC DEFINITIONS
app = Flask(__name__)


class Base(DeclarativeBase):
  pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"



db = SQLAlchemy(model_class=Base)

db.init_app(app)

# ==============================================================================================================
# CREATING BOOK TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# ==============================================================================================================
# CREATING RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()