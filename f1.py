from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# =========================  Task 1 ========================= 
@app.route('/products/<cat>', methods=['GET'])
def get_category(cat):
    api_url = f"https://fakestoreapi.com/products/category/{cat}"
    try:
        # try to get a response from the api we are trying to communicate to
        resp = requests.get(api_url)

        if resp.status_code == 200:
            # all good
            products = resp.json()
            return jsonify(products), 200

        else:
            # error
            return jsonify({"error" : "Category not found"}), 404

    except Exception as e:
        return jsonify({"error" : str(e)}), 500

# ========================= Task 2 ========================= 
@app.route('/add-product', methods=['POST'])
def add_product():
    product_data = request.get_json()
    api_url = "https://fakestoreapi.com/products/"
    try:
        response = requests.post(api_url, json=product_data)
        if response.status_code == 200:
            # All is good
            new_prod = response.json()
            return jsonify(new_prod), 201
        else:
            return jsonify({"error" : "Failed to POST product"}), response.status_code

    except Exception as e:
        return jsonify({"error" : str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
