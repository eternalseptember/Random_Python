'''
myfile = open("test.txt", "w")
myfile.write("This file was generated by Python.\n")
myfile.write("----------------------------------\n")
myfile.write("Hello World!\n")
myfile.close()

filehandle = open("test.txt", "r")
while True:
	theline = filehandle.readline()
	if len(theline) == 0:
		break

	print(theline, end="")

filehandle.close()

# Read list of names and then sort them alphabetically
f = open("list_of_names.txt", "r")
listofnames = f.readlines()
f.close()

listofnames.sort()

g = open("list_of_names_sorted.txt", "w")
for name in listofnames:
	g.write(name)
g.close()

# read the whole file at once
f = open("alice_in_wonderland.txt")
content = f.read()
f.close()

words = content.split()
print("There are {0} words in the file.".format(len(words)))

# copy one binary file to another
f = open("test.zip", "rb")
g = open("test_copy.zip", "wb")

while True:
	buf = f.read(1024)
	if len(buf) == 0:
		break
	g.write(buf)

f.close()
g.close()
'''

