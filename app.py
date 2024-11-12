from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fake Store API URL
API_URL = "https://fakestoreapi.com/products"

@app.route('/')
def index():
    # Fetch products from the Fake Store API
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        products = response.json()  # Parse JSON response
    else:
        products = []

    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
