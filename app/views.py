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

# This route redirects to 
# the home route.
@app.route('/Data Dictionary')
def data_dictionary():
	return redirect(url_for('home'))

# This route goes through 
# a selected project by
# using the python library
# os to find the specific 
# paths and files and displaying
# what are within the files.
@app.route('/<newdir>')
def goto_dir(newdir):

	path = find_dir(newdir) # uses the variable newdir to find the next path within the data dictionary directory
	previous = get_previous(path) # uses the path to get the previous path 
	projects = get_projects(path) # gets the files or data within a specific path
	t_count = 0
	for x in projects:
		if '.xlsx' in x: # checking to see if whats in project is the excel file containing the meta, Can be modified for the different excel extentions.
			t_count+=1
		else:
			t_count-=1
	if t_count == len(projects) and t_count != 0: # if the statement is true then display 3 is activated.
		data = build_table(get_data_set_path(newdir)) # This grabs that variable name and label from with the excel file.
		display = 3
		return render_template('home.html', data = data, display = display, previous = previous)

	display = 2 # Display 2 is activated when a project has been selected and there are more folders within the project representing the different years. 
	return render_template('home.html', projects = projects, display = display, previous = previous)

# This route displays the supporting 
# data from the variable name and label when clicked
# display 4 is activaed in this route.
@app.route('/<newdir>/data')
def display_data(newdir):
	global data_set
	try:
		heading = get_data_set_heading() # gets the headings for the supporting data
		table  = get_data_set(newdir) # gets the supporting data
		results = zip(heading, table) # convert the heading and the data into a tuple so it can be easly displayed
		display = 4
		return render_template('home.html', results = results, display = display)
	except Exception as e:
		return redirect(url_for('error_page')) # redirects to a error page if there is any form of malfunction.
		# example error: if the server has restarted while on display 4. The global variable data_set will be
		# undefined. It is important in order to displaying the supporting datas.

@app.route('/about')
def about_page():
	return render_template('about.html')

# This route is for any scenario that 
# may cause an error. This route displays
# a error that routes back to the home page.
@app.route('/error')
def error_page():
	return render_template('error.html')


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

# This function gets the path to
# projects excel file.
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

# This function uses python xlrd library
# to get the data in the variable name and label.
def build_table(path):

	global workbook
	workbook = xlrd.open_workbook(path)

	global data_set
	data_set = workbook.sheet_by_name("Data Dictionary")

	v_name_col = get_var_pos('Variable name') # gets the column position of the variable name
	v_label_col = get_var_pos('Variable label') # gets the column position of the variable label

	data_name = []
	data_label = []

	for row in range(data_set.nrows - 1):
		data_name.append(str(data_set.cell(row + 1, v_name_col).value))
		data_label.append(str(data_set.cell(row + 1, v_label_col).value)) 

	data = zip(data_name, data_label)
	return data

# This function search the position of
# the top column within the excel file
def get_var_pos(var):
	
	global data_set

	for col in range(data_set.ncols):
		if str(data_set.cell(0, col).value) == var:
			return col

# This function gets the position of the
# variable name clicked in display 3.
def get_data_set_pos(row, name):
	
	global data_set
	for pos in range(data_set.nrows):
		if str(data_set.cell(pos, row).value) == name:
			return pos

# This funcion uses the position collected
# from get_data_set_pos to get the supporting
# data for display 4.
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

# This function gets the heading for 
# the supporting data for display 4.
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