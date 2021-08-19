# Import into the main sudoku_solver class.
"""
Naked triple:
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""


def check_naked_triples(self):
	# self.check_naked_triples_row(4)
	self.check_naked_triples_rows()


def check_naked_triples_rows(self):
	for j in range(9):
		print('looking for naked triples in row: {0}'.format(j))
		self.check_naked_triples_row(j)
		print()

	# self.solve_queue()


def check_naked_triples_row(self, row_num):
	poss_trip_list = {}  # poss_trip_list[coord_str] = [poss_vals]

	# Collect candidate cells and their possibilities first.
	for i in range(9):
		this_cell = (row_num, i)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) > 3:
				continue
			else:
				# Convert cells to string as key.
				subset_str = '{0},{1}'.format(row_num, i)
				poss_trip_list[subset_str] = poss_vals

	# for testing
	print('possible triples candidates?')
	for coord_str in poss_trip_list.keys():
		cell_poss = poss_trip_list[coord_str]
		print('({0}): {1}'.format(coord_str, cell_poss))

	# Analyze if triple exists.
	# trip_set, trip_coords = self.find_naked_triple(poss_trip_list)
	# self.clean_triple_row(trip_set, trip_coords, row_num)


	# ENUMERATING AND TESTING POSSIBLE TRIPLETS
	self.find_naked_triple(poss_trip_list)


def clean_triple_row(self, trip_set, trip_coords, row_num):
	# remove triple vals in cells outside the triple
	for i in range(9):
		this_cell = (row_num, i)
		# if this_cell is in trip_coords, ... skip?
		# if it's not, then remove cells in trip_set

		if this_cell in trip_coords:
			continue
		elif this_cell not in self.possible_values:
			continue
		else:
			poss_vals = self.possible_values[this_cell]

			# remove triples in cells outside the trip_coords
			for trip_val in trip_set:
				if trip_val in poss_vals:
					poss_vals.remove(trip_val)

			# reassign
			self.possible_values[this_cell] = poss_vals

			# check if there's only one value left?
			if len(poss_vals) == 1:
				if (this_cell not in self.solved_list) and \
					(this_cell not in self.solved_queue):
					self.solved_queue.append(this_cell)







"""
def find_naked_triple(self, poss_trip_list):
	# List of all possible triplets.
	# poss_triplets[trip_vals] = [coords]
	# only add after a possible triplet is formed
	poss_triplets = {}

	# How to identify group?
	trip_set = []  # possible values in a possible triplet. Max 3.
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
"""


def find_naked_triple(self, poss_trip_list):
	# make a list of every merged triplet set
	poss_triplets = []

	for item in poss_trip_list.keys():
		# decode the key for the coordinate first
		coord_str = str(item)
		coord = tuple(map(int, coord_str.split(',')))

		# get values in that coord
		# then combine and find valid possible triplets

		poss_vals = poss_trip_list[item]
		print('poss_vals {0} in {1}'.format(coord_str, poss_vals))

















def check_naked_triples_col(self):
	col = 4
	poss_trip_list = {}  # poss_trip_list[coord_str] = [poss_vals]

	# Collect candidate cells and their possibilities first.
	for j in range(9):
		this_cell = (j, col)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) > 3:
				continue
			else:
				# Convert cells to string as key.
				subset_str = '{0},{1}'.format(j, col)
				poss_trip_list[subset_str] = poss_vals

	# for testing
	for coord_str in poss_trip_list.keys():
		cell_poss = poss_trip_list[coord_str]
		print('({0}): {1}'.format(coord_str, cell_poss))

	# cleanup
	trip_set, trip_coords, col_num = self.find_naked_triple(poss_trip_list)
	self.clean_triple_col(trip_set, trip_coords, col_num)
	# self.solve_queue()




def clean_triple_col(self, trip_set, trip_coords, col_num):
	# remove triple vals in cells outside the triple
	for j in range(9):
		this_cell = (j, col)















