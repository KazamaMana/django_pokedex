import requests
import json
import random
URL = "https://pokeapi.co/api/v2/pokemon/"



def pokedex_request(pokemon_value):
    url_request = URL + pokemon_value
    
    pokemon_json = requests.get(url_request)
    return pokemon_json.json()



def json_parse(raw_data):
    pokemon_move = [moves['move']['name'] for moves in raw_data['moves']]
    pokemon_type = [types['type']['name'] for types in raw_data['types']]
    pokemon_type = "/".join(pokemon_type)
    pokemon_data ={
        "name":'',
        "type":'',
        "weight":'',
        "height":'',
        "moves":'',
        "sprites":''
    }
    pokemon_data['name'] = raw_data['name']
    pokemon_data['type'] = pokemon_type
    pokemon_data['weight'] = raw_data['weight']
    pokemon_data['height'] = raw_data['height']
    pokemon_data['moves'] = random.sample(pokemon_move,4)
    pokemon_data['sprite'] = raw_data['sprites']['front_default']
    
    return pokemon_data