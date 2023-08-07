#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Soup, Ingredient, SoupIngredient

# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

class Soups(Resource):
    pass

api.add_resource(Soups, '/soups')

class Ingredients(Resource):
    pass
api.add_resource(Ingredients, '/ingredients')

class IngredientsById(Resource):
    pass

api.add_resource(IngredientsById, '/ingredients/<int:id>')

class SoupIngredients(Resource):
    pass

api.add_resource(SoupIngredients, '/soup_ingredients')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

