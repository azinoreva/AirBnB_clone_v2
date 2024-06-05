#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" A script that starts a web app using storage for fetching data from engine
Routes:
    /states: display a HTML page inside tag BODY
    H1: States
    UL: with the list of all State objects in present DB sorted by name
        LI: description of one State: <state.id>: <B><state.name><B>

    /states/<id>: display a HTML page inside the tag BODY
    if a State object is found with this id:
        H1: State
        H3: Cities
        UL: with the list of City objects linked to State sorted by name
            LI: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
            H1: Not found
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Returns an HTML page of all States sorted by name """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with info about <id>, if it exists."""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> e7f9cf6290d15753a4d2b94029653f08a9a3a8ee
