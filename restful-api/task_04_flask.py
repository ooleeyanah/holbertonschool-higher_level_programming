#!/usr/bin/python3
"""
Module to create an API with Flask.

"""
from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """Root endpoint that welcomes users to the Flask API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return API status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user data for a specific username."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the system."""
    try:
        # Parse JSON data
        data = request.get_json()

        # Check if request body is valid JSON
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400

        # Check if username is provided
        if 'username' not in data:
            return jsonify({"error": "Username is required"}), 400

        username = data['username']

        # Check if username already exists
        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        # Add user to storage
        users[username] = data

        # Return confirmation
        return jsonify({
            "message": "User added",
            "user": data
        }), 201

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
