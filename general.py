import os


def create_directory(directory):
	if not os.path.exists(directory):
		print("creating directory " + directory)
		os.mkdir(directory)
	else:
		print("directory %s already exists" %directory)


create_directory('alphaman')