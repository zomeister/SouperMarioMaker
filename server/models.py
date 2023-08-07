from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Soup(db.Model, SerializerMixin):
    __tablename__ = 'soups'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    soup_ingredients = db.relationship('SoupIngredient', back_populates='soup')
    ingredients = association_proxy('soup_ingredients', 'ingredient')
    
    def __repr__(self):
        return f"<id: {self.id}, {self.name}>"
    

class Ingredient(db.Model, SerializerMixin):
    __tablename__ = 'ingredients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    soup_ingredients = db.relationship('SoupIngredient', back_populates='ingredient')
    soups = association_proxy('soup_ingredients', 'soup')
    
    def __repr__(self):
        return f"<id: {self.id}, {self.name}>"
    
class SoupIngredient(db.Model, SerializerMixin):
    __tablename__ = 'soup_ingredients'
    
    id = db.Column(db.Integer, primary_key=True)
    
    soup_id = db.Column(db.Integer, db.ForeignKey('soups.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
    
    soup = db.relationship('Soup', back_populates='soup_ingredients')
    ingredient = db.relationship('Ingredient', back_populates='soup_ingredients')
    
    def __repr__(self):
        return f"<id: {self.id}, {self.name}>"