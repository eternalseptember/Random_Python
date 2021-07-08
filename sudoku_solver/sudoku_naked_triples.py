# Import into the main sudoku_solver class.
"""
Naked triple:
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""


def check_naked_triples(self):
	self.check_naked_triples_row()



def check_naked_triples_row(self):
	# Collect candidate cells and their possibilities first.
	row = 4
	poss_trip_list = {}  # poss_trip_list[coord_str] = [poss_vals]

	for i in range(9):
		this_cell = (row, i)


		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) > 3:
				continue
			else:
				# Convert cells to string as key.
				subset_str = '{0},{1}'.format(row, i)
				poss_trip_list[subset_str] = poss_vals


	for coord_str in poss_trip_list.keys():
		cell_poss = poss_trip_list[coord_str]
		print('{0}: {1}'.format(coord_str, cell_poss))


	possible_subsets = self.find_naked_triple(poss_trip_list)
	# self.clean_hidden_subsets()



def find_naked_triple(self, poss_trip_list):
	# How to identify group?
	trip_set = []  # possible triplet values
	trip_coords = []  # coords in trip_set



	for item in poss_trip_list.keys():
		# decode the key for the coordinate first
		coord_str = str(item)
		coord = tuple(map(int, coord_str.split(',')))

		poss_vals = poss_trip_list[item]  # used for comparison in this loops

		if len(trip_set) == 0:  # might not be three poss vals at first
			trip_set = poss_vals[:]
			trip_coords.append(coord)

		elif len(trip_set) == 3:  # just compare for now
			# if it is part of the triple, then add the coordinates to the list?
			part_of_triple = True

			for poss_val in poss_vals:
				if poss_val not in trip_set:  # not part of the ref triple
					continue

			# if made it down here, then all values

		else:  # if 1 or 2 poss vals, then see if trip_set needs to be merged
			# unless len(trip_set) + len(poss_vals) > 3
			print()

	return trip_coords





