from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_file(filename):
    """Read and parse data from JSON file"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, filename)

        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return None

def read_csv_file(filename):
    """Read and parse data from CSV file"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, filename)

        data = []
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id and price to appropriate types
                row['id'] = int(row['id'].strip())
                row['price'] = float(row['price'].strip())
                row['name'] = row['name'].strip()
                row['category'] = row['category'].strip()
                data.append(row)
        return data
    except (FileNotFoundError, ValueError, KeyError) as e:
        return None

def filter_products_by_id(products, product_id):
    """Filter products list by ID"""
    if not products:
        return None

    for product in products:
        if product['id'] == product_id:
            return [product]  # Return as list for template consistency
    return []  # Empty list means ID not found

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_data = []
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        items_file_path = os.path.join(current_dir, 'items.json')

        with open(items_file_path, 'r') as file:
            data = json.load(file)
            items_data = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_data = []

    return render_template('items.html', items=items_data)

@app.route('/products')
def products():
    """Handle products route with source and optional id parameters"""
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Initialize variables
    products_data = []
    error_message = None

    # Validate source parameter
    if source not in ['json', 'csv']:
        error_message = "Wrong source"
        return render_template('product_display.html', 
                             products=products_data, 
                             error_message=error_message)

    # Read data based on source
    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')

    # Check if file reading failed
    if products_data is None:
        error_message = f"Error reading {source.upper()} file"
        products_data = []
        return render_template('product_display.html', 
                             products=products_data, 
                             error_message=error_message)

    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = filter_products_by_id(products_data, product_id)

            if filtered_products is None:
                error_message = "Error processing product data"
                products_data = []
            elif len(filtered_products) == 0:
                error_message = "Product not found"
                products_data = []
            else:
                products_data = filtered_products

        except ValueError:
            error_message = "Invalid product ID"
            products_data = []

    return render_template('product_display.html', 
                         products=products_data, 
                         error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)