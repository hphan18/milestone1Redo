from dotenv import find_dotenv, load_dotenv
import requests
import os


load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3"

def movieData(movie_id):
    query_params = {"api_key": os.getenv("TMDB_API_KEY")}
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}",
        params=query_params

    )
    print(response)
    json_response = response.json()
    
    title = json_response["title"]
    tagline = json_response["tagline"]
    poster_path = json_response["poster_path"]
    genre_objects = json_response["genres"]
    genres = ", ".join([genre["name"]for genre in genre_objects])

    poster_url = get_full_poster_url(poster_path)


    return(title, tagline, genres, poster_url)

def get_full_poster_url(poster_path):
    query_params = {"api_key": os.getenv("TMDB_API_KEY")}
    response = requests.get(
        f"{BASE_URL}/configuration",
        params=query_params,
    )
    response_json = response.json()

    base_url = response_json["images"]["base_url"]
    poster_sizes = response_json["images"]["poster_sizes"]
    poster_size = "w500" if "w500" in poster_sizes else poster_sizes[0]

    return f"{base_url}/{poster_size}/{poster_path}"