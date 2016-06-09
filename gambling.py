import random

'''
# Create a black box object that generates random numbers
rng = random.random()
print (rng)

dice_throw = random.randrange(1, 7) # Return an int, one of 1,2,3,4,5,6
print (dice_throw)

r_odd = random.randrange(1, 100, 2) # Random odd number
print (r_odd)

# Generate ints [0...51], representing a deck of cards
cards = list(range(52))
random.shuffle(cards)
print(cards)
'''

def make_random_ints(num, lower_bound, upper_bound):
	""" 
	Generate a list containing num random ints between lower_bound
	and upper_bound. upper_bound is an open bound.
	"""
	rng = random.Random()
	result = []
	for i in range(num):
		result.append(rng.randrange(lower_bound, upper_bound))
	return result


def make_random_ints_no_dups(num, lower_bound, upper_bound):
	"""
	Generate a list containing num random ints between
	lower_bound and upper_bound. upper_bound is an open bound.
	The result list cannot contain duplicates.
	"""
	result = []
	rng = random.Random()
	for i in range(num):
		while True:
			candidate = rng.randrange(lower_bound, upper_bound)
			if candidate not in result:
				break
		result.append(candidate)
	return result



random_integers = make_random_ints(5, 1, 13) # Pick 5 random month numbers.
print("{0}".format(random_integers))

xs = list(range(1,13))		# Make list 1..12 (there are no duplicates)
rng = random.Random()		# Make a random number generator
rng.shuffle(xs)				# Shuffle the list
result = xs[:5]				# Take the first five elements
print(result)

xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)