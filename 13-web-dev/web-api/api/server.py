# flask api
from flask import Flask, request, jsonify
# import cors flask
from flask_cors import CORS
# cors flask


app = Flask(__name__)
CORS(app)

@app.route('/api/contact', methods=['GET'])
def get_contact_info():
    contact_info = {
        "email": "contact@example.com",
        "phone": "123-456-7890"
    }
    return jsonify(contact_info)

# login route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # For simplicity, we are using a hardcoded username and password
    if username == 'user' and password == 'password':
        # Generate a token (in a real application, use JWT or similar)
        token = 'secret-token'
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# products route, should be protected, so check authorization header
@app.route('/api/products', methods=['GET'])
def get_products():
    auth_header = request.headers.get('Authorization')
    if auth_header == 'Bearer secret-token':
        products = [
            {"id": 1, "name": "Product 1", "price": 10.0},
            {"id": 2, "name": "Product 2", "price": 20.0},
            {"id": 3, "name": "Product 3", "price": 30.0}
        ]
        return jsonify(products)
    else:
        return jsonify({"error": "Unauthorized"}), 401

#about route
@app.route('/api/about', methods=['GET'])
def get_about_info():
    about_info = {
        "title": "About Us",
        "content": "We are a company dedicated to providing the best products."
    }
    return jsonify(about_info)

# home 
@app.route('/api/home', methods=['GET'])
def get_home_info():
    home_info = {
        "title": "Welcome to Our Store",
        "description": "Explore our wide range of products."
    }
    return jsonify(home_info)

if __name__ == '__main__':
    app.run(debug=True)