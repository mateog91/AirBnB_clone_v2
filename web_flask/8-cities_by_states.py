#!/usr/bin/python3
"""methods for flask"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def p_states():
    states = storage.all(State).values()
    """renders states"""
    return render_template("8-cities_by_states.html",
                           states=states)


@app.teardown_appcontext
def teardown(self):
    """closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
