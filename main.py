import os

#Each webiste you crawled is a separate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print "Creating project %s"%(directory)
        os.makedirs(directory)

# Create new file
def write_file(path, data):
    handler = open(path, 'w')
    handler.write(data)
    handler.close()

# Create queue and crawled files (if not created)
def create_data_file(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,base_url)

#add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

#delete file content of the file
def delete_file_contents(path):
    with open(path,'w'):
        #Do nothing
        pass

#Convert each line to the set item (for duplicate)
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Iterate through a set, each item will be a new linr
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        print link



