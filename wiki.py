import requests

def get_wikipedia_link(movie_title):
    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "prop": "info",
            "inprop": "url",
            "titles": [f"{movie_title}"],
        },
    )
    response_json = response.json()
    
    url = next(iter(response_json["query"]["pages"].values()))["fullurl"]
    return url