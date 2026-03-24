from flask import Flask, render_template, request
import json
import csv
import sqlite3
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
            # Read all lines and strip whitespace
            lines = [line.strip() for line in file.readlines()]
            
            # Create CSV reader from cleaned lines
            import io
            cleaned_csv = io.StringIO('\n'.join(lines))
            csv_reader = csv.DictReader(cleaned_csv)
            
            for row in csv_reader:
                # Convert id and price to appropriate types, strip all values
                cleaned_row = {}
                for key, value in row.items():
                    cleaned_row[key.strip()] = value.strip()
                
                cleaned_row['id'] = int(cleaned_row['id'])
                cleaned_row['price'] = float(cleaned_row['price'])
                data.append(cleaned_row)
        return data
    except (FileNotFoundError, ValueError, KeyError) as e:
        return None

def read_sqlite_database(db_filename, product_id=None):
    """Read and parse data from SQLite database"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, db_filename)
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        if product_id:
            # Query for specific product ID
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            # Query for all products
            cursor.execute("SELECT id, name, category, price FROM Products")
        
        rows = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries for template consistency
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2], 
                'price': row[3]
            })
        
        return data
    except (sqlite3.Error, FileNotFoundError) as e:
        print(f"Database error: {e}")
        return None

def filter_products_by_id(products, product_id):
    """Filter products list by ID"""
    if not products:
        return None
        
    for product in products:
        if product['id'] == product_id:
            return [product]
    return []

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
    if source not in ['json', 'csv', 'sql']:
        error_message = "Wrong source"
        return render_template('product_display.html', 
                             products=products_data, 
                             error_message=error_message)
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')
    elif source == 'sql':
        if product_id:
            try:
                product_id = int(product_id)
                products_data = read_sqlite_database('products.db', product_id)
            except ValueError:
                error_message = "Invalid product ID"
                products_data = []
                return render_template('product_display.html', 
                                     products=products_data, 
                                     error_message=error_message)
        else:
            products_data = read_sqlite_database('products.db')
    
    # Check if file/database reading failed
    if products_data is None:
        error_message = f"Error reading {source.upper()} {'database' if source == 'sql' else 'file'}"
        products_data = []
        return render_template('product_display.html', 
                             products=products_data, 
                             error_message=error_message)

    if product_id and source != 'sql':
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
    
    # For SQL source, check if no products were found when ID was specified
    elif product_id and source == 'sql' and len(products_data) == 0:
        error_message = "Product not found"
        products_data = []
    
    return render_template('product_display.html', 
                         products=products_data, 
                         error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)