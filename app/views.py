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

@app.route('/Data Dictionary')
def data_dictionary():
	return redirect(url_for('home'))


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
		data = build_table(get_data_set_path(newdir))
		display = 3
		return render_template('home.html', data = data, display = display, previous = previous)

	display = 2
	return render_template('home.html', projects = projects, display = display, previous = previous)

@app.route('/<newdir>/data')
def display_data(newdir):
	heading = get_data_set_heading()
	table  = get_data_set(newdir)
	display = 4
	return render_template('home.html', table = table, heading = heading, display = display)


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
	xfile = os.listdir(file)
	if len(xfile) > 1:
		for x in xfile:
			if x.startswith('.'):
				num = xfile.index(x)
				xfile.pop(num)
				break
	file = file + '/' + xfile[0]

	return file

def build_table(path):
	print path

	global workbook
	workbook = xlrd.open_workbook(path)

	global data_set
	data_set = workbook.sheet_by_name("Data Dictionary")

	v_name_col = get_var_pos('Variable name')
	v_label_col = get_var_pos('Variable label')

	# for col in range(data_set.ncols):
	# 	if str(data_set.cell(0,col).value) == 'Variable name':
	# 		v_name_col = (col)
	# 	if str(data_set.cell(0,col).value) == 'Variable label':
	# 		v_label_col = (col)

	data_name = []
	data_label = []

	for row in range(data_set.nrows - 1):
		data_name.append(str(data_set.cell(row + 1, v_name_col).value))
		data_label.append(str(data_set.cell(row + 1, v_label_col).value)) 

	data = zip(data_name, data_label)
	return data

def get_var_pos(var):
	
	global data_set

	for col in range(data_set.ncols):
		if str(data_set.cell(0, col).value) == var:
			return col

def get_data_set_pos(row, name):
	
	global data_set
	for pos in range(data_set.nrows):
		if str(data_set.cell(pos, row).value) == name:
			return pos

def get_data_set(var):

	global data_set

	v_name_col = get_var_pos('Variable name')
	v_label_col = get_var_pos('Variable label')

	pos = get_data_set_pos(v_name_col, var)

	data = []

	for row in range(data_set.ncols):
		if row != v_name_col and row != v_label_col:
			data.append(str(data_set.cell(pos, row).value))

	print(str(data))

	return data


def get_data_set_heading():

	v_name_col = get_var_pos('Variable name')
	v_label_col = get_var_pos('Variable label')

	global data_set

	head = []
	for row in range(data_set.ncols):
		if row != v_name_col and row != v_label_col:
			head.append(str(data_set.cell(0, row).value))
	
	print('######## ' + str(head) + '########' )
	return head

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port="5000")