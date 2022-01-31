#!/usr/bin/python3
"""methos for flask"""

from email.policy import strict
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def p_states():
    """renders states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(self):
    """closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
