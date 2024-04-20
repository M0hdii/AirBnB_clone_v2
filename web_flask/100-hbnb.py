#!/usr/bin/python3
"""
This script Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ this func Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ this func displays C + some text """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """ this func displays python + some text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ this func displays n only if it s an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display an HTML page with the number n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    this func displays an HTML page with the number n and a message
    """
    return render_template(
            '6-number_odd_or_even.html',
            n=n,
            message='even' if n % 2 == 0 else 'odd')


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a list of all states """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a list of all cities of a certain state """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """
    Display a list of all cities of a certain state with and id
    """
    if id:
        states = storage.all(State).get(f"State.{id}", None)
    else:
        states = storage.all(State).values()
        sorted_states = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=sorted_states, id=id)

    return render_template(
                '9-states.html', states=states, id=id)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays html page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
            "10-hbnb_filters.html",
            states=states, amenities=amenities)


@app.route("/hbnb", strict_slashes=False)
def hbnb_place():
    """Displays html page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template(
            "100-hbnb.html",
            states=states, amenities=amenities, places=places)



@app.teardown_appcontext
def teardown(exception):
    """ Close the Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
