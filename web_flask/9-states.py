#!/usr/bin/python3
"""methods for flask"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def p_states(id=None):
    states = storage.all(State)
    print(states)
    """renders states"""
    if(id):
        key_id = "State." + id
        if key_id in states:
            state = states[key_id]
            print("im am here")
        else:
            state = None

        return render_template("9-states.html",
                               state=state, id=id)
    else:
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
