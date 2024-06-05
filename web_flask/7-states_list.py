#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
=======
""" A script that starts a web app using storage for fetching data from engine
Routes:
    /states_list: display a HTML page inside tag BODY
    H1: States
    UL: with the list of all State objects in present DB
        LI: description of one State: <state.id>: <B><state.name><B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State


>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
<<<<<<< HEAD
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
=======
    """ Returns an HTML page of all States sorted by name """
    states = storage.all(State)
>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
def teardown_appcontext(exception):
    """ Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
