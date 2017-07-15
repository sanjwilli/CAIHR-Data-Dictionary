import os
import xlrd

# path = os.getcwd() + '/Data Dictionary'
# file = os.listdir(path)

# # for x in file:
# # 	print(x)

# def goto_dir():
# 	di = str(raw_input('Enter path: '))
# 	global path
# 	path = path + '/' + di

# 	print(path)

# 	print(os.listdir(path))
# 	

# def find(name):
# 	for root, dirs, files in os.walk(os.getcwd() + "/Data Dictionary"):
# 		if name in root:
# 			if root.endswith(name):
# 				print(root,name)
# 		#print(root)
# 	print("finish")

# try:
# 	s = raw_input("name: ")
# 	find(s)
# except:
# 	print("Could not find")
# 	

path = os.getcwd() + '/Data Dictionary/The Spanish Town arm of the International Study of Hypertension in Blacks/JYRRBS_THE OFFICIAL DATA DICTIONARY AND TABLES June 17 2016.xlsx'

workbook = xlrd.open_workbook(path)
data_set = workbook.sheet_by_name("Data Dictionary")
# sheet = workbook.sheet_by_name("Data Dictionary")
# sheet.cell_value(0,0)
# sheet.nrows
# sheet.ncols

for col in range(data_set.ncols):
	if str(data_set.cell(0,col).value) == 'Variable name':
		v_name_col = (col)
	if str(data_set.cell(0,col).value) == 'Variable label':
		v_label_col = (col)

data_name = []
data_label = []

for row in range(20):
	data_name.append(str(data_set.cell(row+1, v_name_col).value))
	data_label.append(str(data_set.cell(row + 1, v_label_col).value))

# data = zip(data_name, data_label)

#print(data)
# for x,y in zip(data_name, data_label):
# 	print x + '\t\t\t' + y
	
#print type(data)

# for col in range(sheet.ncols):
# 	print sheet.cell_value(0,col)

# sheet.cell_type(1,2)
# exceltime = sheet.cell_value(1,2)
# time_tuple = xlrd.xldate_as_tuple(exceltime, 0)
# datetime.datetime(*time_tuple)
# if __name__ == '__main__':
# 	goto_dir()
# 	print(path)