#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, jsonify, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api, Migrate, Flask
# Add your model imports
from models import Soup, Ingredient, SoupIngredient

# Views go here!


class Soups(Resource):
    def get(self):
        return make_response([s.to_dict(rules = ('-soup_ingredients',)) for s in Soup.query.all()])

api.add_resource(Soups, '/soups')

class SoupsById(Resource):
    def get(self, id):
        soup = Soup.query.filter_by(id = id).first()
        if not soup:
            return make_response({'error': 'That soup does not exist yet.'}, 404)
        return make_response(soup.to_dict(), 200)

api.add_resource(SoupsById, '/soups/<int:id>')

class Ingredients(Resource):
    def get(self):
        return make_response([i.to_dict(rules = ('-soup_ingredients',)) for i in Ingredient.query.all()])

api.add_resource(Ingredients, '/ingredients')

class IngredientsById(Resource):
    def get(self, id):
        ingredient = Ingredient.query.filter_by(id = id).first()
        if not ingredient:
            return make_response({'error': 'That ingredient does not exist yet.'}, 404)
        return make_response(ingredient.to_dict(), 200)

api.add_resource(IngredientsById, '/ingredients/<int:id>')

class SoupIngredients(Resource):
    def get(self):
        return make_response([s_i.to_dict() for s_i in SoupIngredient.query.all()])

api.add_resource(SoupIngredients, '/soup_ingredients')



if __name__ == '__main__':
    app.run(port=5555, debug=True)

