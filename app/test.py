import os

path = os.getcwd() + '/Data Dictionary'
file = os.listdir(path)

# for x in file:
# 	print(x)

def goto_dir():
	di = str(raw_input('Enter path: '))
	global path
	path = path + '/' + di

	print(path)

	print(os.listdir(path))



if __name__ == '__main__':
	goto_dir()
	print(path)