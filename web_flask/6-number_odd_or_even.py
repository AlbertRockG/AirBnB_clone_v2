#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Displays "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "HBNB!"
    """
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    Displays "C" followed by the value of text
    variable.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """
    Displays "Python" followed by the value
    of text variable.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    Displays "n is a number" only if n is an integer.
    """
    return "{} is a number".format(str(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page with H1 tag: "Number: n"
    inside the tag BODY.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays a HTML page with H1: "Number: n is even|odd" inside BODY."""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port))
