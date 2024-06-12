import logging
from flask import Flask, request, jsonify, render_template
from models import db, Flavor, Ingredient, Allergen, ProductType, Suggestion, Cart
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice_cream_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    flavors = Flavor.query.all()
    ingredients = Ingredient.query.all()
    allergens = Allergen.query.all()
    product_types = ProductType.query.all()
    cart = Cart.query.all()
    return render_template('index.html', flavors=flavors, ingredients=ingredients, allergens=allergens, product_types=product_types, cart=cart)

@app.route('/filter_offerings', methods=['GET'])
def filter_offerings():
    flavor_query = request.args.get('flavor', '')
    ingredient_query = request.args.get('ingredient', '')
    allergen_query = request.args.get('allergen', '')
    product_type_query = request.args.get('product_type', '')

    query = Flavor.query

    if flavor_query:
        query = query.filter(Flavor.name.like(f'%{flavor_query}%'))
    if ingredient_query:
        query = query.join(Ingredient).filter(Ingredient.name.like(f'%{ingredient_query}%'))
    if allergen_query:
        query = query.join(Ingredient).join(Allergen).filter(Allergen.name.like(f'%{allergen_query}%'))
    if product_type_query:
        query = query.join(ProductType).filter(ProductType.name.like(f'%{product_type_query}%'))

    flavors = query.all()

    result = []
    for flavor in flavors:
        ingredients = [ingredient.name for ingredient in flavor.ingredients]
        allergens = [allergen.name for ingredient in flavor.ingredients for allergen in ingredient.allergens]
        result.append({
            'id': flavor.id,
            'name': flavor.name,
            'season': flavor.season,
            'ingredients': ingredients,
            'allergens': allergens
        })

    return jsonify(result)

@app.route('/suggestions', methods=['POST'])
def suggestions():
    data = request.form
    customer_name = data['customer_name']
    flavor_suggestion = data['flavor_suggestion']
    
    suggestion = Suggestion(customer_name=customer_name, flavor_suggestion=flavor_suggestion)
    db.session.add(suggestion)
    db.session.commit()
    
    return jsonify({'message': 'Suggestion submitted successfully!'})

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.form
    flavor_id = data['flavor_id']
    product_type_id = data['product_type_id']
    
    cart_item = Cart(flavor_id=flavor_id, product_type_id=product_type_id)
    db.session.add(cart_item)
    db.session.commit()
    
    return jsonify({'message': 'Added to cart successfully!'})


if __name__ == '__main__':
    with app.app_context():
        init_db(app)
    app.run(debug=True)
