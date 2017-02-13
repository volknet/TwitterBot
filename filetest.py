import re

file_handle = open('putfile.txt', 'r')
readFile = file_handle.readlines()

for line in readFile:
	data = line.strip()

search = re.search('text:', data)
if search:
	print(search)
