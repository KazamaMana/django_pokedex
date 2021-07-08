import requests
import json
import random
URL = "https://pokeapi.co/api/v2/pokemon/"



def pokedex_request():
    pkmn_name = input('Name or Pokemon ID ')
    url_request = URL + pkmn_name
    
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
        "moves":''
    }
    pokemon_data['name'] = raw_data['name']
    pokemon_data['type'] = pokemon_type
    pokemon_data['weight'] = raw_data['weight']
    pokemon_data['height'] = raw_data['height']
    pokemon_data['moves'] = random.sample(pokemon_move,4)
    
    return pokemon_data