from api import app
from flask import Flask, jsonify


@app.route('/')
def get_data():
    return jsonify({'data': 'Hello from Flask!'})