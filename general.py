import os

def create_dir(directory):
	if not os.path.exists(directory):
		print("creating directory: " +directory)
		os.makedirs(directory)

	else:
		print("directory already exists")


create_dir("w3schools")


#https: // www.w3schools.com / python / default.asp


def create_data_files(project_name, base_url):
	queue = project_name +  '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_files(queue, base_url)
	if not os.path.isfile(crawled):
		write_files(crawled, '')


def write_files(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

create_data_files('w3schools', 'https: // www.w3schools.com / python / default.asp')


def append_to_files(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')


#deleting the data
def delete_files(path):
	with open(path, 'w') :
		pass



