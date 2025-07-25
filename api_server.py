
import os
import json
from flask import Flask, jsonify, abort

app = Flask(__name__)

# The root directory of your project where the JSON files are located.
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return "Welcome to the AL/OL Papers API!"

@app.route('/api/<path:filepath>')
def get_data(filepath):
    """
    This endpoint serves the content of a specific JSON file.
    The path to the file is provided in the URL.
    For example, to get the content of 25al/home.json, the URL would be:
    /api/25al/home.json
    """
    # Construct the full path to the JSON file
    file_path = os.path.join(DATA_DIR, f"{filepath}.json")

    # Check if the file exists
    if not os.path.exists(file_path):
        return abort(404)  # Return a 404 Not Found error if the file doesn't exist

    # Read the JSON data from the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    return jsonify(data)

@app.route('/api/files')
def list_files():
    """
    This endpoint returns a list of all available JSON files.
    """
    files = []
    for root, dirs, filenames in os.walk(DATA_DIR):
        for filename in filenames:
            if filename.endswith('.json'):
                # Get the relative path of the file
                relative_path = os.path.relpath(os.path.join(root, filename), DATA_DIR)
                files.append(relative_path)
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True)
