from flask import Flask, render_template
import json
import os

app = Flask(__name__)

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
    # Read items from items.json
    items_data = []
    try:
        # Get the current directory path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        items_file_path = os.path.join(current_dir, 'items.json')

        # Read and parse the JSON file
        with open(items_file_path, 'r') as file:
            data = json.load(file)
            items_data = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # If file doesn't exist or JSON is invalid, use empty list
        items_data = []

    return render_template('items.html', items=items_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
