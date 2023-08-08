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

    def post(self):
        data = request.json
        try:
            soup = Soup(name = data['name'],)
        except ValueError as v_error:
            return make_response({'errors':[str(v_error)]}, 422)
        except KeyError as e_error:
            return make_response({'errors':[str(e_error)]}, 422)
        
        db.session.add(soup)
        db.session.commit()
        return make_response(soup.to_dict(rules = ('-soup_ingredients',)), 201)

api.add_resource(Soups, '/soups')

class SoupsById(Resource):
    def get(self, id):
        soup = Soup.query.filter_by(id = id).first()
        if not soup:
            return make_response({'error': 'That soup does not exist yet.'}, 404)
        return make_response(soup.to_dict(), 200)
    
    def patch(self, id):
        soup = Soup.query.filter_by(id = id).first()
        if not soup:
            return make_response({'error': 'That soup does not exist yet.'}, 404)
        data = request.json
        for key in data:
            try:
                setattr(soup, key, data[key])
            except ValueError as v_error:
                return make_response({'errors': [str(v_error)]}, 422)
        db.session.commit()
        return make_response(soup.to_dict(rules = ('-soup_ingredients',)))

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
    
    def delete(self, id):
        ingredient = Ingredient.query.filter_by(id = id).first()
        if not ingredient:
            return make_response({'errors':'Ingredient is out of stock.'}, 404)
        db.session.delete(ingredient)
        db.session.commit()
        return make_response('', 204)

api.add_resource(IngredientsById, '/ingredients/<int:id>')

class SoupIngredients(Resource):
    def get(self):
        return make_response([s_i.to_dict() for s_i in SoupIngredient.query.all()])
    
    def post(self):
        data = request.json
        try:
            soup_ingredient = SoupIngredient(soup_id=data['soup_id'], ingredient_id=data['ingredient_id'], name=data['name'])
        except ValueError as v_error:
            return make_response({'errors': [str(v_error)]}, 422)
        db.session.add(soup_ingredient)
        db.session.commit()
        return make_response(soup_ingredient.to_dict(), 204)

api.add_resource(SoupIngredients, '/soup_ingredients')

class SoupIngredientsById(Resource):
    def get(self, id):
        soup_ingredient = SoupIngredient.query.filter_by(id = id).first()
        if not soup_ingredient:
            return make_response({'error': 'That custom soup does not exist yet.'}, 404)
        return make_response(soup_ingredient.to_dict(), 200)
    
    def delete(self, id):
        soup_ingredient = SoupIngredient.query.filter_by(id = id).first()
        if not soup_ingredient:
            return make_response({'errors':'That custom soup does not exist.'}, 404)
        db.session.delete(soup_ingredient)
        db.session.commit()
        return make_response('', 204)

api.add_resource(SoupIngredientsById, '/soup_ingredients/<int:id>')

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

