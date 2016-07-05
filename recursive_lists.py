def recur_sum(nested_num_list):
	total = 0
	for element in nested_num_list:
		if type(element) == type([]):
			total += recur_sum(element)
		else:
			total += element

	return total


total = recur_sum([1, 2, [11, 13], 8])
print("Total: {0}".format(total))