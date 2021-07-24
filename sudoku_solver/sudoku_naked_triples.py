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


	trip_set, trip_coords = self.find_naked_triple(poss_trip_list)
	# self.clean_hidden_subsets()



def find_naked_triple(self, poss_trip_list):
	# How to identify group?
	trip_set = []  # possible triplet values. Max 3.
	trip_coords = []  # coords in trip_set. Max 3.

	# Keep track of which poss_trip_list has been used for comparison.
	poss_trip_keys = poss_trip_list.keys()


	for item in poss_trip_keys:
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
					part_of_triple = False
					continue

			if part_of_triple:
				trip_coords.append(coord)

		else:  # see if two lists could be merged together
			combined_poss = list(set(trip_set+poss_vals))

			if len(combined_poss) > 3:
				# coord not part of triple as referenced by trip_set
				return
			else:
				# combine the two set of coords and re-run the comparison
				trip_set = combined_poss
				trip_coords.append(coord)

	print('combined set: {0}'.format(trip_set))


	return trip_set, trip_coords




def clean_triple_row(self, trip_set, trip_coords, row_num):
	# remove triple vals in cells outside the triple
	for i in range(9):
		this_cell = (row_num, i)
		# if this_cell is in trip_coords, ... skip?
		# if it's not, then remove cells in trip_set






