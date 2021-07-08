# serve.py
from api import pokedex_request
from api import json_parse
from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    response = pokedex_request()
    pokemon_data = (json_parse(response))
    return render_template('index.html', pokemon_data=pokemon_data)

# run the application
if __name__ == "__main__":
    app.run(debug=True)
    
