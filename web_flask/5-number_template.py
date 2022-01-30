#!/usr/bin/python3
"""methods for flask web framework"""

from flask import Flask, render_template
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


@app.route('/c/<text>')
def hello_hbnb3(text):
    """/c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'})
@ app.route('/python/<text>')
def hello_hbnb4(text):
    """/python/(<text>): display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space ) """
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>')
def hello_hbnb5(n):
    """display “n is a number” only if n is an integer
    Args:
        n [int]: a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def hello_hbnb6(n):
    """display “n is a number” only if n is an integer inside the tag BODY
    Args:
        n [int]: a number
    """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
