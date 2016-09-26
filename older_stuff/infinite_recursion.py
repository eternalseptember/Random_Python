def recursion_depth(number):
	print("Recursion depth number", number)
	try:
		recursion_depth(number + 1)
	except:
		print("I cannot go any deeper into this wormhole.")
		# Stops after r997



recursion_depth(0)