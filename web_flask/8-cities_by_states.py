#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
=======
""" A script that starts a Flask web app, To load all cities of State
if storage is DCStorage, must use cities relationship otherwise use
public getter method cities.
Routes:
    /cities_by_states: Display a HTML page inside tag BODY
    H1: States
    UL: tag with list of all State obj in present DBStorage and sorted
        LI: description of one State:<state.id>: <B><state.name></B> + UL:
        with list if City objects linked to the State sorted by name
            LI: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State


>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
<<<<<<< HEAD
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
    """Returns a HTML page sorted by name"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Removes the current SQLALchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
