from models import db, Flavor, Ingredient, Allergen, ProductType

def init_db(app):
    with app.app_context():
        db.create_all()

        # Add seed data for flavors
        flavors = [
            Flavor(name='Vanilla', season='Summer'),
            Flavor(name='Chocolate', season='Winter'),
            Flavor(name='Strawberry', season='Spring'),
            Flavor(name='Mint', season='Autumn'),
            Flavor(name='Caramel', season='Spring'),
            Flavor(name='Coffee', season='Winter'),
            Flavor(name='Blueberry', season='Summer'),
            Flavor(name='Pistachio', season='Autumn'),
            Flavor(name='Coconut', season='Spring'),
            Flavor(name='Banana', season='Summer'),
        ]

        db.session.bulk_save_objects(flavors)
        db.session.commit()

        # Retrieve saved flavors from the database
        flavors = Flavor.query.all()

        # Add seed data for ingredients
        ingredients = [
            Ingredient(name='Milk', flavor_id=flavors[0].id),
            Ingredient(name='Sugar', flavor_id=flavors[0].id),
            Ingredient(name='Cocoa', flavor_id=flavors[1].id),
            Ingredient(name='Strawberry', flavor_id=flavors[2].id),
            Ingredient(name='Mint extract', flavor_id=flavors[3].id),
            Ingredient(name='Caramel syrup', flavor_id=flavors[4].id),
            Ingredient(name='Coffee extract', flavor_id=flavors[5].id),
            Ingredient(name='Blueberry puree', flavor_id=flavors[6].id),
            Ingredient(name='Pistachio nuts', flavor_id=flavors[7].id),
            Ingredient(name='Coconut milk', flavor_id=flavors[8].id),
            Ingredient(name='Banana puree', flavor_id=flavors[9].id),
        ]

        db.session.bulk_save_objects(ingredients)
        db.session.commit()

        # Retrieve saved ingredients from the database
        ingredients = Ingredient.query.all()

        # Add seed data for allergens
        allergens = [
            Allergen(name='Lactose', ingredient_id=ingredients[0].id),
            Allergen(name='Lactose', ingredient_id=ingredients[1].id),
            Allergen(name='Nuts', ingredient_id=ingredients[7].id),
            Allergen(name='Nuts', ingredient_id=ingredients[9].id),
        ]

        db.session.bulk_save_objects(allergens)
        db.session.commit()

        # Add seed data for product types
        product_types = [
            ProductType(name='Cone'),
            ProductType(name='Bar'),
            ProductType(name='Cup'),
            ProductType(name='Sandwich'),
            ProductType(name='Stick'),
            ProductType(name='Bite'),
            ProductType(name='Sorbet'),
            ProductType(name='Soft Serve'),
            ProductType(name='Gelato'),
            ProductType(name='Frozen Yogurt'),
        ]

        db.session.bulk_save_objects(product_types)
        db.session.commit()
