from os.path import split

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

#-------------------- Load_dotenv Values -----------------------#
load_dotenv()

TMDB_MOVIE_SEARCH_URL = os.getenv("TMDB_MOVIE_SEARCH_URL")
TMDB_API_READ_ACCESS_TOKEN = os.getenv("TMDB_API_READ_ACCESS_TOKEN")
TMDB_MOVIE_INFO_URL = os.getenv("TMDB_MOVIE_INFO_URL")
TMDB_MOVIE_IMG_URL = os.getenv("TMDB_MOVIE_IMG_URL")

#-------------------- App Initializer -----------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

#-------------- Forms Built using FlaskForm -----------------#
class UpdateMovieRatingForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

#------------------------ Database Section ---------------------#
# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# #Remember: Run this context switch once
# with app.app_context():
#     db.create_all()
#
# ## After adding the new_movie the code needs to be commented out/deleted.
# ## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

#---------------------- Routes Section --------------------------#
@app.route("/")
def home():
    #The .order_by(Movie.rating) naturally arranges in ascending order
    all_movies = db.session.execute(db.select (Movie).order_by(Movie.rating)).scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    # #Descending order - if you wish to put in such order
    # # Change .order_by(Movie.rating) to include .desc() 👇
    # all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    #
    # for i in range(len(all_movies)):
    #     # Simply assign the rank based on its index position!
    #     all_movies[i].ranking = i + 1
    #
    # db.session.commit()

    return render_template("index.html", movies=all_movies)

# Adding the Update functionality
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = UpdateMovieRatingForm()
    # Fetch the movie out of the if statement here so that it's ready right away
    movie_to_update = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:id>")
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_READ_ACCESS_TOKEN}",
        }
        parameters = {
            "query": movie_title,
            "include_adult": False,
            "language": "en-US",
            "page": 1
        }

        response = requests.get(TMDB_MOVIE_SEARCH_URL, headers=headers, params=parameters)
        data = response.json()["results"]

        return render_template("select.html", options=data)

    return render_template("add.html", form=form)

@app.route("/find/<int:id>", methods=["GET", "POST"])
def find(id):
    if id:
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_READ_ACCESS_TOKEN}",
        }

        response = requests.get(f"{TMDB_MOVIE_INFO_URL}{id}", headers=headers)
        data = response.json()
        # print(data)

        movie_title = data.get("title")
        movie_date = data.get("release_date")
        movie_description = data.get("overview")
        movie_img_url = f"{TMDB_MOVIE_IMG_URL}{data.get('poster_path')}"

        new_movie = Movie(
            title = movie_title,
            year = movie_date.split('-')[0],
            description = movie_description,
            img_url = movie_img_url
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
