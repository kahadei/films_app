import requests
from myjson.json_worker import dict_to_json

films = ['Spider-man: No way to home', 'Crazy Stupid Love.',
         'Die Hard',
         'Dead Poets Society',
         'Home Alone',
         'Seven',
         'Memento',
         'Harry Potter and the Prisoner of Azkaban'
         "One Flew Over the Cuckoo's Nest"
         ]


def get_film_id(query="Die Hard"):
    url_movie_by_title = "https://moviesminidatabase.p.rapidapi.com/movie/imdb_id/byTitle/" + query
    headers = {
        "X-RapidAPI-Key": "2cbe1506f2msh8afa3a8d1441a0ep1fd5b0jsn32e39521aff9",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }
    response = requests.request("GET", url_movie_by_title, headers=headers)
    respons_dict = response.json()
    return respons_dict

data = get_film_id()
print(data)

dict_to_json(data)
