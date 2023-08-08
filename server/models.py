from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class Soup(db.Model, SerializerMixin):
    __tablename__ = 'soups'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    soup_ingredients = db.relationship('SoupIngredient', back_populates='soup')
    ingredients = association_proxy('soup_ingredients', 'ingredient')
    
    @validates('name')
    def validate_soup_name(self, key, new_soup_name):
        if not new_soup_name:
            raise ValueError('Please give the soup a name.')
        return new_soup_name

    def __repr__(self):
        return f"<id: {self.id}, {self.name}>"
    

class Ingredient(db.Model, SerializerMixin):
    __tablename__ = 'ingredients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    soup_ingredients = db.relationship('SoupIngredient', back_populates='ingredient')
    soups = association_proxy('soup_ingredients', 'soup')

    serialize_rules = ('-soup_ingredients.ingredient','-soup_ingredients.soup.soup_ingredients')
    
    def __repr__(self):
        return f"<id: {self.id}, {self.name}>"
    
class SoupIngredient(db.Model, SerializerMixin):
    __tablename__ = 'soup_ingredients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    soup_id = db.Column(db.Integer, db.ForeignKey('soups.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
    
    soup = db.relationship('Soup', back_populates='soup_ingredients')
    ingredient = db.relationship('Ingredient', back_populates='soup_ingredients')

    serialize_rules = ('-soup.soup_ingredients', '-ingredient.soup_ingredients',)

    @validates
    def validate_soup_ingredients_name(self, key, new_soup_ingredients_name):
        if not new_soup_ingredients_name:
            raise ValueError('Please give the new soup a name!.')
        return new_soup_ingredients_name

    @validates
    def validate_soup_id(self, key, new_soup_id):
        if not new_soup_id:
            raise ValueError('There must be a soup id.')
        return new_soup_id
    
    @validates
    def validate_ingredient_id(self, key, new_ingredient_id):
        if not new_ingredient_id:
            raise ValueError('There must be a ingredient id.')
        return new_ingredient_id
    
    def __repr__(self):
        return f"<id: {self.id}, {self.name}>"