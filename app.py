import flask
import random
from tmdb import movieData
from wiki import get_wikipedia_link
import os

app = flask.Flask(__name__)

MOVIE_IDS = [
    335787,
    414906,
    508947,
]

@app.route("/")
def main():
    movie_id = random.choice(MOVIE_IDS)
    (title, tagline, genres, poster_url) = movieData(movie_id)
    wiki_url = get_wikipedia_link(title)
    return flask.render_template(
        "main.html",
        title=title,
        tagline=tagline,
        genres=genres,
        poster_url=poster_url,
        )

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=os.getenv("PORT", 8080)
)
