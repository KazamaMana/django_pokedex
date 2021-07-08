from models import pokedex_request
from models import json_parse

def main():
    response = pokedex_request()
    print(json_parse(response))


if __name__ == '__main__':
    main()