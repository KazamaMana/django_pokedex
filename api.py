import requests
import json
import random
from flask import Response

URL = "https://pokeapi.co/api/v2/pokemon/"



def pokedex_request(pokemon_value):
    url_request = URL + pokemon_value
    
    pokemon_json = requests.get(url_request)
    return pokemon_json.json()



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
    pokemon_data['moves'] = ','.join(pokemon_move)
    pokemon_data['sprite'] = raw_data['sprites']['front_default']
    
    return pokemon_data