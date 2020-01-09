import os

def create_directory(directory):
	if not os.path.exists(directory):
		print("creating directory : " + directory)
		os.makedirs(directory)
	else:
		print("%s already exists" %directory)


create_directory('alphaman')