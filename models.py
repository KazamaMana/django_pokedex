# utils
from utils import get

def pokedex_request():
    pokemon_json = get(url='https://pokeapi.co/api/v2/pokemon/zigzagoon/')
    return pokemon_json

