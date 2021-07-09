# serve.py
from api import pokedex_request
from api import json_parse
from flask import Flask, request
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# creates a Flask application, named app
def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    
    return app

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html', pokemon_data="")

@app.route("/post_field", methods=["GET", "POST"])
def need_input():
    form_value = request.form['pokemon_value']
    response = pokedex_request(form_value)
    pokemon_data = (json_parse(response))
    return render_template('index.html', pokemon_data=pokemon_data)

# run the application
if __name__ == "__main__":
    app.run(debug=True)
    
