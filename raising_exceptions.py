def get_age():
	age = int(input("Please enter your age: "))
	if age < 0:
		# Create a new instance of an exception
		error = ValueError("{0} is not a valid age.".format(age))
		raise error
		# raise ValueError("{0} is not a valid age.".format(age))
	return age


get_age()