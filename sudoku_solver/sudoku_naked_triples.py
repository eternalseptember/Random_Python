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
	"""
	for j in range(9):  # j is row number
		self.check_naked_triples_row(j)
	"""

	j = 4
	# print('looking for naked triples in row: {0}'.format(j))
	self.check_naked_triples_row(j)

	# self.solve_queue()


def check_naked_triples_row(self, row_num):
	poss_trip_list = []

	# Collect candidate cells and their possibilities first.
	for i in range(9):  # i is col number
		this_cell = (row_num, i)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) <= 3:
				# look up the possible values later
				poss_trip_list.append(this_cell)


	# Analyze if triple exists.
	poss_triplets = self.find_naked_triples(poss_trip_list)









def find_naked_triples(self, poss_trip_list):
	# make a list of every merged triplet set
	poss_trip_coords = {}  # [trip_str] = [list of coords]
	number_of_cells = len(poss_trip_list)

	for cell in range(number_of_cells-1):
		cell_1 = poss_trip_list[cell]
		cell_2 = poss_trip_list[cell+1]

		item_1 = self.possible_values[cell_1]
		item_2 = self.possible_values[cell_2]
		combined_poss = sorted(list(set(item_1 + item_2)))
		trip_str = ''.join(map(str, combined_poss))
		trip_coords = [cell_1, cell_2]

		# Two cells that combined have fewer than 3 possible combinations are
		# taken care by other functions.
		if len(combined_poss) <= 3:
			if trip_str not in poss_trip_coords:  # new possible triplet
				poss_trip_coords[trip_str] = trip_coords

				print('cell 1: {0}\tcell 2: {1}'.format(cell_1, cell_2))
				print('combined set: {0}'.format(combined_poss))

			else:  # otherwise, add coords to existing entry
				saved_info = poss_trip_coords[trip_str]

				for coord in trip_coords:
					if coord not in saved_info:
						saved_info.append(coord)

				# update dictionary with new list?
				poss_trip_coords[trip_str] = saved_info


	# look at the dictionary
	print('what\'s getting passed?')
	for poss_trip in poss_trip_coords:
		coords = poss_trip_coords[poss_trip]
		print('key {0}: item {1}'.format(poss_trip, coords))


	# compare length of list. need 3 coords
	items_to_remove = []


	return poss_trip_coords







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
			self.check_if_solved(this_cell, poss_vals)






















def check_naked_triples_col(self):
	col = 4
	poss_trip_list = []




def clean_triple_col(self, trip_set, trip_coords, col_num):
	# remove triple vals in cells outside the triple
	for j in range(9):
		this_cell = (j, col)















