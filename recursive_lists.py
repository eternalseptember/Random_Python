from modules.test import *


def recur_sum(nested_num_list):
	total = 0
	for element in nested_num_list:
		if type(element) == type([]):
			total += recur_sum(element)
		else:
			total += element

	return total


def recur_max(nested_list):
	"""
	Find the maximum in a recursive structure of lists
	within other lists.
	Precondition: No lists or sublists are empty.
	"""
	largest = None
	first_time = True
	for element in nested_list:
		if type(element) == type([]):
			value = recur_max(element)
		else:
			value = element

		if first_time or value > largest:
			largest = value
			first_time = False

	return largest



total = recur_sum([1, 2, [11, 13], 8])
print("Total: {0}".format(total))

test(recur_max([2, 9, [1, 13], 8, 6]) == 13)
test(recur_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
test(recur_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
test(recur_max(["joe", ["sam", "ben"]]) == "sam")