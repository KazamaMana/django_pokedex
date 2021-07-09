import requests
import random
from flask import Response

URL = "https://pokeapi.co/api/v2/pokemon/"



def pokedex_request(pokemon_value):
    url_request = URL + pokemon_value
    pokemon_json = dict()
    pokemon_json['name'] = ''
    pokemon_json['type'] = ''
    pokemon_json['weight'] = ''
    pokemon_json['height'] = ''
    pokemon_json['moves'] = ''
    pokemon_json['sprite'] = ''
    pokemon_response = requests.get(url_request)
    print(pokemon_response.status_code)
    if pokemon_response.status_code == 200:
        pokemon_json = pokemon_response.json()
        pokemon_json['message'] = "OK"
        pokemon_json['status_code'] = pokemon_response.status_code
    else:
        pokemon_json['message'] = "Pokemon not found"
        pokemon_json['status_code'] = pokemon_response.status_code

    return pokemon_json



def json_parse(raw_data):
    pokemon_move_list = [moves['move']['name'] for moves in raw_data['moves']]
    pokemon_type = [types['type']['name'] for types in raw_data['types']]
    pokemon_type = "/".join(pokemon_type)
    pokemon_move = random.sample(pokemon_move_list,4)
    pokemon_data ={
        "name":'',
        "type":'',
        "weight":'',
        "height":'',
        "moves":'',
        "sprites":''
    }
    pokemon_data['name'] = raw_data['name'].capitalize()
    pokemon_data['type'] = pokemon_type.capitalize()
    pokemon_data['weight'] = raw_data['weight']/10
    pokemon_data['height'] = raw_data['height']*10
    pokemon_data['moves'] = pokemon_move
    pokemon_data['sprite'] = raw_data['sprites']['front_default']
    
    return pokemon_data