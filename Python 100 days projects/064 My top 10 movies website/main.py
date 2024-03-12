from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests






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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


all_movies = []



class Base(DeclarativeBase):
  pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-top-10-movies.db"



db = SQLAlchemy(model_class=Base)

db.init_app(app)

# ==============================================================================================================
# CREATING MOVIE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)
    ranking: Mapped[str] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()







# ==============================================================================================================
# FLASK PAGE DEFINITIONS


@app.route('/')
def home():
    # Getting movies from database
    with app.app_context():
        result = db.session.query(Movie).all()  # Search all movies
        movies = [{
                    "title": movie.title, 
                    "year": movie.year, 
                    "description": movie.description,
                    "rating": movie.rating,
                    "ranking": movie.ranking,
                    "review": movie.review,
                    "img_url": movie.img_url
                } for movie in result]

    # Renderizing template with books
    return render_template("index.html", movies=movies)



# ==============================================================================================================
# CREATING RECORD

# FIRST MOVIE:
try:
    with app.app_context():
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
except Exception:
    pass

# SECOND MOVIE:
try:
    with app.app_context():
        second_movie = Movie(
            title="Avatar The Way of Water",
            year=2022,
            description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
            rating=7.3,
            ranking=9,
            review="I liked the water.",
            img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        )
        db.session.add(second_movie)
        db.session.commit()
except Exception:
    print(Exception)
# ==============================================================================================================


# ADD THE MOVIE
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        information = {
            "title": request.form["title"],
            "year": request.form["year"],
            "description": request.form["description"],
            "rating": request.form["rating"],
            "ranking": request.form["ranking"],
            "review": request.form["review"],
            "img_url": request.form["img_url"]

        }
        all_movies.append(information)
        # ==============================================================================================================
        # CREATING RECORD
        try:
            with app.app_context():
                new_movie = Movie(
                    title=information["title"],
                    year=information["year"],
                    description=information["description"],
                    rating=information["rating"],
                    ranking=information["ranking"],
                    review=information["review"],
                    img_url=information["img_url"],
                )
                db.session.add(new_movie)
                db.session.commit()
        except Exception:
            pass
        # ==============================================================================================================


        return redirect(url_for('home'))       
    return render_template("add.html")



@app.route("/delete/<movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    with app.app_context():
        movie_to_delete = Movie.query.get(movie_id)
        if movie_to_delete:
            db.session.delete(movie_to_delete)
            db.session.commit()
        return redirect(url_for('home'))
    



if __name__ == "__main__":
    app.run(debug=True)







'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

