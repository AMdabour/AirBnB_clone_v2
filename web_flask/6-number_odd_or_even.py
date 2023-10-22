#!/usr/bin/python3
""" a script that starts a Flask web application: """
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns a hello message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def dynamic_C(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dynamic_python(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """checks if n is a number 'int'"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """returns a HTML response"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """returns HTML reponse with odd or even n"""
    if n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    return render_template('6-number_odd_or_even.html', n=n, state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
