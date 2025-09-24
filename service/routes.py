from flask import Flask, jsonify, request
from myapp.models import Product  # Adjust import for your ORM

app = Flask(__name__)

# ---------------- READ ----------------
@app.route('/products/<int:product_id>', methods=['GET'])
def read_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "availability": product.availability
    }), 200


# ---------------- UPDATE ----------------
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.availability = data.get("availability", product.availability)
    product.save()
    
    return jsonify({"message": "Product updated successfully"}), 200


# ---------------- DELETE ----------------
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    product.delete()
    return jsonify({"message": "Product deleted successfully"}), 204


# ---------------- LIST / SEARCH ----------------
@app.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')

    products = Product.get_all()

    if name:
        products = [p for p in products if p.name.lower() == name.lower()]
    if category:
        products = [p for p in products if p.category.lower() == category.lower()]
    if availability is not None:
        availability_bool = availability.lower() == 'true'
        products = [p for p in products if p.availability == availability_bool]

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "availability": p.availability
        })
    
    return jsonify(result), 200
