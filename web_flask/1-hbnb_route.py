#!/usr/bin/python3
"""methods for flask web framework"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Write a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb2():
    """ displays HBNB for this route /hbnb”
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
