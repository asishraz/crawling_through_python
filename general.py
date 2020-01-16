import os

def create_dir(directory):
	if not os.path.exists(directory):
		print("creating directory: " +directory)
		os.makedirs(directory)
	else:
		print("directory already exists")


create_dir(input("Enter the directory name: "))


def create_data_files(project, base_url):
	queue = project + 'queue.txt'
	crawled = project + 'crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

#create a new file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

