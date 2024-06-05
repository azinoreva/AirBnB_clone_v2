#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a flask app and added function for var if integer """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python2text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number2text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
""" A script that starts a flask web app listening on 0.0.0.0, port 5000
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display C followed by value of text variable
    /python/<text>: display Python followed by value of text variable
    value of text is "is cool".
    /number/<n>: display "n is a number" only if n is an integer
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# New dynamic route
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Replace underscores with spaces in the text"""
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)


# New route for /python/<text> with default value "is cool"
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    display_text = text.replace('_', ' ')
    return 'Python {}'.format(display_text)


# New route for /number/<n> that displays only if n is an int
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    # çonfigure the app to listen on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
