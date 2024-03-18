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
    author: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# ==============================================================================================================
"""
CREATE
"""
# CREATING RECORD
# NOTE: When creating new records, the primary key fields is optional. you can also write:
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


with app.app_context():
    new_book2 = Book(id=2, title="Harry Potter 2", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book2)
    db.session.commit()

with app.app_context():
    new_book3 = Book(id=3, title="Harry Potter 3", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book3)
    db.session.commit()

with app.app_context():
    new_book4 = Book(id=4, title="Harry Potter 4", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book4)
    db.session.commit()
# ==============================================================================================================
"""
READ
"""
# READING RECORDS
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
# ==============================================================================================================
# READING A PARTICULAR RECORD BY QUERY
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(book)
    print(all_books)



# ==============================================================================================================
"""
UPDATE
"""
# Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 

# ==============================================================================================================
# Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  


# ==============================================================================================================
"""
DELETE
"""
# Delete A Particular Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()