#!/usr/bin/python3
"""methods for flask web framework"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hello_hbnb2():
    """ displays HBNB for this route /hbnb”
    """
    return 'HBNB'


@app.route('/c/<text>')
def hello_hbnb3(text):
    """/c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'C {}'.format(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
