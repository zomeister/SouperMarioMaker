#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Soup, Ingredient, SoupIngredient

        
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
        s1 = Soup(name='Mushroom Kingdom Minestrone', image='https://images.themodernproper.com/billowy-turkey/production/posts/2019/Hungarian-Mushroom-Soup-6.jpg?w=1200&q=82&fm=jpg&fit=crop&dm=1601404554&s=82e3710364c62425e799ad7291becd57')
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
        s9 = Soup(name="Princess Peach's Pea Puree", image='https://butterwithasideofbread.com/wp-content/uploads/2021/06/Chilled-Peach-Soup-recipe-09.jpg')
        soups.append(s9)
        s10 = Soup(name="Bowser's Beefy Borscht", image="https://images.themodernproper.com/billowy-turkey/production/posts/2020/Italian-Meatball-Soup-17.jpg?w=1800&q=82&fm=jpg&fit=crop&dm=1601404668&s=ccb3236e942090571c47c5f27a4f7f82")
        s11 = Soup(name="Mario's Miso Adventure Ramen", image="https://images.themodernproper.com/billowy-turkey/production/posts/2016/White-Bean-Chicken-Soup-6.jpg?w=1800&q=82&fm=jpg&fit=crop&dm=1685667626&s=1b1e3b1c3ea8d1bba2d49618828faa64")
        soups.append(s11)
        
        ingredients = []
        i1 = Ingredient(name="Douglas", image="https://www.douglas.ca/wp-content/uploads/DB-Logo-Red-wOriginal.png")
        ingredients.append(i1)
        i2 = Ingredient(name="Toad Heads", image="https://m.media-amazon.com/images/I/6149l+eQqkL._AC_UF894,1000_QL80_.jpg")
        ingredients.append(i2)
        i3 = Ingredient(name="Goomba Feet", image="https://pbs.twimg.com/media/E5J_leOVoAM6Z0w.jpg:large")
        ingredients.append(i3)
        i4 = Ingredient(name="Koopa Breast", image="https://houseofsmokeinc.com/wp-content/uploads/2021/09/turtle-meat.jpg")
        ingredients.append(i4)
        i5 = Ingredient(name="Koopa Stock", image="https://images.delightedcooking.com/slideshow-mobile-small/soup-stock.jpg")
        ingredients.append(i5)
        i6 = Ingredient(name="Thwomp Spikes", image="https://i.redd.it/ce8wkjy36o071.jpg")
        ingredients.append(i6)
        i7 = Ingredient(name="Wiggler Flower", image="https://www.petalrepublic.com/wp-content/uploads/2022/07/75-Popular-Types-of-White-Flowers-With-Names-Pictures.jpeg")
        ingredients.append(i7)
        i8 = Ingredient(name="Birdo Beak", image="https://www.beefmagazine.com/sites/beefmagazine.com/files/uploads/2012/04/retail-73-27-frozen-strand_0.jpg")
        ingredients.append(i8)
        i9 = Ingredient(name="Yoshi Egg", image="https://mario.wiki.gallery/images/thumb/4/42/NSMBU_Green_Yoshi_Egg_Artwork.png/1200px-NSMBU_Green_Yoshi_Egg_Artwork.png")
        ingredients.append(i9)
        i10 = Ingredient(name="Yoshi Egg (hardboiled)", image="https://mario.wiki.gallery/images/thumb/4/42/NSMBU_Green_Yoshi_Egg_Artwork.png/1200px-NSMBU_Green_Yoshi_Egg_Artwork.png")
        ingredients.append(i10)
        i11 = Ingredient(name="Gold Mushroom", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReMTS_phNYLnkJVHj2BrNe80gQbVIicykkAw&usqp=CAU")
        ingredients.append(i11)
        i12 = Ingredient(name="Fire Mushroom", image="https://img.freepik.com/premium-photo/fire-mushroom_839169-15197.jpg")
        ingredients.append(i12)
        i13 = Ingredient(name="Ice Mushroom", image="https://i.dailymail.co.uk/1s/2019/01/09/15/8315556-0-Miniature_icicles_form_beneath_the_snow_capped_mushrooms_of_ice_-a-25_1547048218448.jpg")
        ingredients.append(i13)
        i14 = Ingredient(name="Hammer-Bro Helmet", image="https://i.etsystatic.com/13413218/r/il/3e3814/1659366616/il_fullxfull.1659366616_nexi.jpg")
        ingredients.append(i14)
        i15 = Ingredient(name="Shy Guy Tears", image="https://images.artwanted.com/large/98/44166_733798.jpg")
        ingredients.append(i15)
        i16 = Ingredient(name="Boo Broth", image="https://perfecthealthdiet.com/wp/wp-content/uploads/2011/10/bb-7.jpg")
        ingredients.append(i16)
            
        soup_ingredients = []
        si1 = SoupIngredient(name="Tasty Mario Soup", image="https://images.freshop.com/00051000207982/ab07a56b0fcf58fb2f3225366553bee8_large.png")
        soup_ingredients.append(si1)
        si2 = SoupIngredient(name="Nasty Soup", image="https://soupmakerguide.co.uk/wp-content/uploads/2018/05/chickentesticle.png")
        soup_ingredients.append(si2)
        si3 = SoupIngredient(name="Very Tasty Soup", image="https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_744,ar_5:4/v1/img/recipes/32/61/60/picUNL72Q.jpg")
        soup_ingredients.append(si3)
        
        # soups = [Soup(name=fake.first_name()) for _ in range(10)]
        # ingredients = [Ingredient(name=fake.name()) for _ in range(20)]
        # soup_ingredients = [SoupIngredient() for _ in range(40)]
        
        db.session.add_all(soups + ingredients + soup_ingredients)
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
