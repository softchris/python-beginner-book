# create flask app
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# product list with template
@app.route("/products-template")
def products_template():
    products_list = [
        {"name": "Product 1", "price": 10.99},
        {"name": "Product 2", "price": 12.99},
        {"name": "Product 3", "price": 15.99}
    ]
    return render_template("products.html", products=products_list) 

# products route
@app.route("/products")
def products():
    # should have page and pageSize

    products_list = [
        {"name": "Product 1", "price": 10.99},
        {"name": "Product 2", "price": 12.99},
        {"name": "Product 3", "price": 15.99}
    ]
    # Simulating pagination
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("pageSize", 10))
    start = (page - 1) * page_size
    end = start + page_size
    products_list = products_list[start:end]

    return {"products": products_list}

# render json
@app.route("/data")
def data():
    return {
        "message": "Hello, World!",
        "status": "success"
    }

# router params
@app.route("/data/<name>")
def data_name(name):
    return {
        "message": f"Hello, {name}!",
        "status": "success"
    }

# url query params
@app.route("/query")
def query_params():
    name = request.args.get("name", "Guest")
    return {
        "message": f"Hello, {name}!",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True) 