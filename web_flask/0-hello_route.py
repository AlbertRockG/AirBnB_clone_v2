#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
import os
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_word():
    """
    Prints "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port))
