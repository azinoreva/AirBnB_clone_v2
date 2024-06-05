#!/usr/bin/python3
<<<<<<< HEAD
""" Adds sixth view func that displays HTML page if n is odd or even """

from flask import Flask
from flask import render_template


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
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """ display html if n is int. """
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ display different page depending on var given odd or even. """
    return render_template('6-number_odd_or_even.html', n=n)


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
    /number_template/<n>: display a HTML page only if n is an int:
        H1 tag: "Number: n" inside the tag BODY
    /number_odd_or_even/<n>: displays HTML page only if n is an int.
        H1 tag: "Number: n is even|odd" inside the tag BODY
"""
from flask import Flask, render_template
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


# new route that displays html file using the render_template
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns an HTML page only if n is an int"""
    return render_template('5-number.html', n=n)


# New route /number_odd_or_even/<n> that displays a page with render_template
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns an HTML if only an int specifying odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    # çonfigure the app to listen on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
