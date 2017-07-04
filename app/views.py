"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os

from app import app
from flask import render_template, request, redirect, url_for, flash

# ----- Views ----- #
@app.route('/')
def home():
	return render_template('home.html')

# ----- Functionalities ----- #


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port="5000")