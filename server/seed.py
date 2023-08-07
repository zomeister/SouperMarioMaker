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
        for _ in range(10):
            soup = Soup(name=fake.first_name())
            soups.append(soup)
        
        ingredients = []
        for _ in range(20):
            ingredient = Ingredient(name=fake.first_name())
            ingredients.append(ingredient)
            
        soup_ingredients = []
        for _ in range(40):
            si = SoupIngredient()
            soup_ingredients.append(si)
        
        # soups = [Soup(name=fake.first_name()) for _ in range(10)]
        # ingredients = [Ingredient(name=fake.name()) for _ in range(20)]
        # soup_ingredients = [SoupIngredient() for _ in range(40)]
        
        db.session.add_all(soups + ingredients + soup_ingredients)
        db.session.commit()
        
        return soups, ingredients, soup_ingredients
def relate_records(soups, ingredients, soup_ingredients):
    with app.app_context():
        for si in soup_ingredients:
            si.ingredient = rc(ingredients)
            si.soup = rc(soups)
            
        db.session.add_all(soup_ingredients)
        db.session.commit()
        return soup_ingredients
    

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        delete_records()
        soups, ingredients, soup_ingredients = create_records()
        soup_ingredients = relate_records(soups, ingredients, soup_ingredients)
        
        # Seed code goes here!