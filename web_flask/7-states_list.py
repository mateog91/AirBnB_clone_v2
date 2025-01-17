#!/usr/bin/python3
"""
Module for task 7 that renders the webpage
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """method teardown that closes correctly a session"""
    storage.close()


@app.route('/states_list')
def states():
    """method states that Display all states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
