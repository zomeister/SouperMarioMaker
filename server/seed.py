#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Soup, Ingredient, SoupIngredient

def delete_records():
    with app.app_context():
        Soup.query.delete()
        Ingredient.query.delete()
        SoupIngredient.query.delete()
        db.session.commit()
    
def create_records():
    with app.app_context():
        
        soups = []
        s1 = Soup(name='Mushroom Kingdom Minestrone', image='https://www.bhg.com/thmb/x_eUYmq2nvGyqk6uSbNCjsqKSuI=/550x0/filters:no_upscale():strip_icc()/R107556-cb94eebcdd24489bb65fa37bc61d76fe.jpg')
        soups.append(s1)
        s2 = Soup(name='Goomba Gumbo', image='https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_1:1/k%2FPhoto%2FSeries%2F2023-01-how-to-make-cajun-gumbo%2F2022-how-to-make-cajun-gumbo__925')
        soups.append(s2)
        s3 = Soup(name='Koopa Chowder', image='https://media-cdn.tripadvisor.com/media/photo-s/07/44/c4/48/our-famous-turtle-chowder.jpg')
        soups.append(s3)
        s4 = Soup(name='Power-Up Pumpkin Bisque', image='https://hellolittlehome.com/wp-content/uploads/2020/11/roasted-pumpkin-soup-2.jpg')
        soups.append(s4)
        s5 = Soup(name="Yoshi's Egg Drop Soup", image='https://drivemehungry.com/wp-content/uploads/2020/07/egg-drop-soup-11.jpg')
        soups.append(s5)
        s6 = Soup(name='Fire Flower Fiery Stew', image='https://lh3.googleusercontent.com/pw/AM-JKLVoesSyVPpeX4lQWo-XAiY8KsW_15B7dzckpgpT1LoZv7hVQ3m_npX0-0KulIEV5phWrpPNZymw3CZHaFuLYTgwPUG6Idqjt5L_xn5ZzG8V3eQk7dO4rL6ymWGEejAEIaefjuBF_-BB90KodqvkxZ8k4g=w500-h375-no?authuser=1')
        soups.append(s6)
        s7 = Soup(name='Starman Spiced Soup', image='https://3.bp.blogspot.com/-jC0O_P9VpFU/VM9G84mVMlI/AAAAAAAAS3E/o-QkkcXNx0M/s1600/star%2Bfish%2Bsea%2Bcoconut%2Bsoup%2B2.jpg')
        soups.append(s7)
        s8 = Soup(name="Luigi's Green Broth", image='https://www.marathonsandmotivation.com/wp-content/uploads/2020/01/DSC03983-scaled.jpg.webp')
        soups.append(s8)
        s9 = Soup(name="Princess Peach's Pea Puree", image='https://www.foodandwine.com/thmb/adCX619Thniagfx2tWl5qUFx204=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/201107-xl-chilled-peach-soup-with-fresh-goat-cheese-2000-bd37ebf458af4b458b33e32930521e02.jpg')
        soups.append(s9)
        s10 = Soup(name="Bowser's Beefy Borscht", image="https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/k%2FPhoto%2FRecipes%2F2020-12-katie-jackson's-short-rib-borscht%2Fk-photo-2020-12-borscht-3")
        soups.append(s10)
        
        ingredients = []
        for _ in range(20):
            ingredient = Ingredient(name=fake.first_name())
            ingredients.append(ingredient)
            
        soup_ingredients = []
        for _ in range(40):
            si = SoupIngredient(name=fake.first_name())
            soup_ingredients.append(si)
        
        # soups = [Soup(name=fake.first_name()) for _ in range(10)]
        # ingredients = [Ingredient(name=fake.name()) for _ in range(20)]
        # soup_ingredients = [SoupIngredient() for _ in range(40)]
        
        db.session.add_all(soups + ingredients)
        db.session.commit()
        
        return soups, ingredients, soup_ingredients
def relate_records(soups, ingredients, soup_ingredients):
    with app.app_context():
        for si in soup_ingredients:
            si.soup = rc(soups)
            si.ingredient = rc(ingredients)
            
        db.session.add_all(soup_ingredients)
        db.session.commit()
        
        return soup_ingredients
    

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        delete_records()
        soups, ingredients, soup_ingredients = create_records()
        soup_ingredients = relate_records(soups, ingredients, soup_ingredients)