from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    season = db.Column(db.String(80), nullable=False)
    ingredients = db.relationship('Ingredient', backref='flavor', lazy=True)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'), nullable=False)
    allergens = db.relationship('Allergen', backref='ingredient', lazy=True)

class Allergen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)

class ProductType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    flavor_suggestion = db.Column(db.String(80), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'), nullable=False)
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'), nullable=False)
    flavor = db.relationship('Flavor', backref=db.backref('cart_items', lazy=True))
    product_type = db.relationship('ProductType', backref=db.backref('cart_items', lazy=True))
