# serve.py
from api import pokedex_request
from api import json_parse
from flask import Flask, request
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import abort


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


@app.route("/pokedex", methods=["GET", "POST"])
def pokedex_card_view():
    form_value = request.form['pokemon_value']
    response = pokedex_request(form_value)
    if response['status_code'] == 200:
        try:
            
            pokemon_data = (json_parse(response))
            return render_template('index.html', pokemon_data=pokemon_data,error_message="")
        except Exception as error:
            return render_template('index.html', pokemon_data=response,error_message="Pokemon Data is not fully updated!")
    else:
        return render_template('index.html',error_message=response['message'],pokemon_data=response)



# run the application
if __name__ == "__main__":
    app.run(debug=True,port=8888,host="0.0.0.0")
    
