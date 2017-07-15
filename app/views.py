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

file_location = app.config['DATA_DICTIONARY_FOLDER']

# ----- Views ----- #

# This routes to the home page 
# and  dispplays the different
# research projects.
@app.route('/')
def home():
	projects = get_projects(app.config['DATA_DICTIONARY_FOLDER'])
	global file_location
	file_location = app.config['DATA_DICTIONARY_FOLDER']
	display = 1
	return render_template('home.html', projects = projects, display = display)

@app.route('/<newdir>')
def goto_dir(newdir):

	path = find_dir(newdir)
	previous = get_previous(path)
	projects = get_projects(path)
	t_count = 0
	for x in projects:
		if '.xlsx' in x:
			t_count+=1
		else:
			t_count-=1
	if t_count == len(projects) and t_count != 0:
		data_name, data_label = build_table(get_data_set_path(newdir))
		display = 3
		return render_template('home.html', data_name = data_name, data_label = data_label, display = display, previous = previous)

	display = 2
	return render_template('home.html', projects = projects, display = display, previous = previous)

@app.route('/<newdir>/data')
def display_data(newdir):
	table  = build_table()
	return render_template('home.html')


# def goto_back():
# 	global file_location
# 	print('######### ' + file_location + ' #########')
# 	rm_point = file_location.rfind('/')
# 	print('######### ' + str(rm_point) + ' #########')
# 	file_location = file_location[:rm_point]
# 	new_rm_point = file_location.rfind('/')
# 	new_path = file_location[new_rm_point+1:]
# 	return redirect(url_for('goto_dir', newdir=new_path))
# 	print('######### changed location : ' + file_location + ' #########')
# 	print('#########  WENT BACK #########')

# app.jinja_env.globals['goto_back'] = goto_back
	

# ----- Functionalities ----- #

# This function returns what is
# listed in a specific folder
# clicked when browsing in
# the data dictionary.
def get_projects(path):
	return os.listdir(path)

# This function provides a path to the
# next path clicked in the data dictionary.
def find_dir(name):
	for root, dirs, files in os.walk(app.config['DATA_DICTIONARY_FOLDER']):
		if name in root and root.endswith(name):
			return root

# This function below provides a link to
# the previous path for the back button 
# on the application when browsing
# the data dictionary.
def get_previous(path):
	point = path.rfind('/')
	path = path[:point]
	point = path.rfind('/')
	path = path[point+1:]
	return path

def get_data_set_path(path):
	file = find_dir(path)
	xfile = file + str(os.listdir(file))
	print xfile
	return xfile

def build_table(path):
	print path
	workbook = xlrd.open_workbook(path)

	data_set = workbook.sheet_by_name("Data Dictionary")

	for col in range(data_set.ncols):
		if str(data_set.cell(0,col).value) == 'Variable name':
			v_name_col = (col)
		if str(data_set.cell(0,col).value) == 'Variable label':
			v_label_col = (col)

	data_name = []
	data_label = []

	for row in range(data_set.nrows - 1):
		data_name.append(str(data_set.cell(row + 1, v_name_col).value))
		data_label.append(str(data_set.cell(row + 1, v_label_col).value)) 

	return data_name, data_label



if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port="5000")