from flask import Flask, request 
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pymongo


app = Flask(__name__)


# Connecting to the Mongo's database
client = pymongo.MongoClient("mongodb+srv://Texuga:Kumulus2021@cluster0.sbi9l.mongodb.net/mousse?retryWrites=true&w=majority")
db = client['mousse']
collection = db['root']


# A schema definition for validating user data
product_schema = {
  "type": "object",
  "properties": {
    "product": {
      "type": "string",
      "minLength": 3
    },
    "description": {
      "type": "string",
      "minLength": 3
    },
    "price": {
      "type": "number",
      "minimum": 0
    }
  },
  "additionalProperties": False
}

prods = []

# Creating a product
@app.route('/products', methods=['POST'])
def new_product():
    prod = request.json

    try:
        validate(instance=prod, schema=product_schema)

    except ValidationError as e:
        return e.message, 400

    # Creating an id for any object
    prod['id'] = len(prods) + 1
    prods.append(prod)

    # Inserting the product in the mongo's database
    var = collection.insert_one(prod)

    return f"New ObjectId Inserted:{str(var.inserted_id)}", 201


# Updating a product
@app.route('/products/<int:prod_id>', methods=['PUT'])
def update_product(id):
    prod = list(filter(lambda x: x['id'] == int(id), prods))

    if not len(prod):
        return 'Product not found', 404

    prod = prod[0]
    update_request = request.json

    try:
        validate(instance=update_request, schema=product_schema)
    except ValidationError as e:
        return e.message, 400

    for key in update_request:
        prod[key] = update_request[key]

    # Updating the product in the mongo's database
    collection.update_one({"id": int(id)}, {"$set": prod})

    return prod


# Deleting a product
@app.route('/products/<int:prod_id>', methods=['DELETE'])
def delete_product(id):
    global prods
    prods = list(filter(lambda x: x['id'] != int(id), prods))

    # Deleting the product from the mongo's database
    collection.delete_one({"id": int(id)})

    return {'message': 'Product deleted'}


# Listing all products
@app.route('/products', methods=['GET'])
def list_products():
    filtered_prods = prods
    filter_prod = request.args.get('product', None)
    
    if filter_prod:
        filtered_prods = filter(lambda x: filter_prod.lower() in x['products'].lower(), filtered_prods)
    return {'products': prods}


if __name__ == '__main__':
    app.run(port=10)