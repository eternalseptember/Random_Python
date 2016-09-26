import urllib.request

# Saves the file to disk
url="http://www.gutenberg.org/cache/epub/5200/pg5200.txt"

'''
destination_filename = "metamorphosis.txt"
urllib.request.urlretrieve(url, destination_filename)
'''

def retrieve_page(url):
	"""
	Retrieve the contents of a web page.
	The contents is converted to a string before returning it.
	The tutorial used readall(), but it had to be changed to read.()
	"""
	socket = urllib.request.urlopen(url)
	stream = str(socket.read())
	socket.close()
	return stream


text = retrieve_page(url)
print (text) # In windows, the console has \r\n instead of a new line