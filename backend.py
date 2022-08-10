import flask

from flask import Flask
from flask_cors import CORS
from flask import request, jsonify

def make_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/hello", methods=["GET"])
    def hello_page():
        return jsonify('hello')

    return app