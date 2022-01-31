#!/usr/bin/python3
"""methos for flask"""

from email.policy import strict
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

states = storage.all(State).values()
cities = storage.all(City).values()


@app.route('/states_list', strict_slashes=False)
def p_states():
    """renders states"""
    return render_template("7-states_list.html", states=states, cities=cities)


@app.teardown_appcontext
def teardown(self):
    """closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
