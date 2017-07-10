"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
import xlrd

from app import app
from flask import render_template, request, redirect, url_for, flash

# ----- Gobal variables ----- #

#file_location = os.getcwd() + '/app/Data Dictionary'

# ----- Views ----- #
@app.route('/')
def home():
	projects = get_projects(app.config['DATA_DICTIONARY_FOLDER'])
	display = 1
	return render_template('home.html', projects = projects, display = display)

@app.route('/<newdir>')
def goto_dir(newdir):
	# global file_location
	# file_location = file_location + '/' + newdir
	path = app.config['DATA_DICTIONARY_FOLDER'] + '/' + newdir
	projects = get_projects(path)
	display = 2
	return render_template('home.html', projects = projects, display = display)


def goto_back():
	return "ok"
	

# ----- Functionalities ----- #


def get_projects(path):
	return os.listdir(path)

def find_dir():
	pass

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port="5000")