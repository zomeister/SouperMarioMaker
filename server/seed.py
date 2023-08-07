#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Soup, Ingredient, SoupIngredient


# def relate_records(soups, ingredients, soup_ingredients):
#     for si  in soup_ingredients:
#         si.soup = rc(soups)
#         si.ingredient
        
fake = Faker()
def delete_records():
    with app.app_context():
        Soup.query.delete()
        Ingredient.query.delete()
        SoupIngredient.query.delete()
        db.session.commit()
    
def create_records():
    with app.app_context():
        
        soups = []
        for i in range(10):
            soup = Soup(name=fake.first_name())
            soups.append(soup)
        db.session.add_all(soups)
        db.session.commit()
        
        ingredients = []
        # for i in range(10):
        #     ingredient = Ingredient(fake.first_name())
        #     ingredients.append(ingredient)
        # db.session.add_all(ingredients)
        
        
        return soups # + ingredients

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # delete_records()
        soups = create_records()
        
        # Seed code goes here!