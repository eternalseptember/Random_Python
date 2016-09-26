eng2sp = {} 			# empty dictionary
eng2sp["one"] = "uno"	# kvp
eng2sp["two"] = "dos"
eng2sp["three"] = "tres"
#eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
'''
for k in eng2sp.keys():	# The order of the k's is not defined
	print("Got key", k, "which maps to value", eng2sp[k])

ks = list(eng2sp.keys())
print(ks)

for k in eng2sp:
	print("Got key", k)

print(list(eng2sp.values())) # can be turned into a list
print(list(eng2sp.items()))  # can be turned into a list of tuples

for (k,v) in eng2sp.items():
	print("Got", k, "that maps to", v)

print("one" in eng2sp)
print("six" in eng2sp)
print("tres" in eng2sp)



inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)
del inventory["pears"]
print(inventory)
inventory["pears"] = 0
print(inventory)
inventory["bananas"] += 200
print(inventory)
print(len(inventory))



opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy() # shallow copy
alias["right"] = "left"
print(opposites["right"]) # prints "left"
copy["right"] = "privilege"
print(opposites["right"]) # prints "left"



#matrix = [[0, 0, 0, 1, 0],
#		  [0, 0, 0, 0, 0],
#		  [0, 2, 0, 0, 0],
#		  [0, 0, 0, 0, 0],
#		  [0, 0, 0, 3, 0]]

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix[(0, 3)])
print(matrix.get((0, 3), 0))
print(matrix.get((1, 3), 0))
'''


# Generate a frequency table for letters
letter_counts = {}
for letter in "Mississippi":
	letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)

letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)