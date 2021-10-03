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
	# Collect candidate cells and their possibilities.
	poss_trip_list = []

	# Get a list of cells that can be part of a triple.
	for i in range(9):  # i is col number
		this_cell = (row_num, i)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) <= 3:
				poss_trip_list.append(this_cell)


	# Analyze if triple exists.
	poss_trips_info = self.find_naked_triples(poss_trip_list)
	self.clean_triple_row(poss_trips_info, row_num)



def clean_triple_row(self, poss_trips_info, row_num):
	# Remove trip possibilities in cells that are not part of the triple.
	for item in poss_trips_info.keys():

		# Decode key and turn it back into a list of numbers.
		trip_set = [int(trip_val) for trip_val in item]
		coords_set = poss_trips_info[item]

		# print('trip set: {0}\t\tcoords set: {1}'.format(trip_set, coords_set))

		# skip over cells that are part of this triple?
		# remove trip values from cells not part of triple
		for i in range(9):  # i is col number
			this_cell = (row_num, i)

			if this_cell not in coords_set:
				if this_cell in self.possible_values:

					# remove values in trip_set from this cell's possible values
					poss_vals = self.possible_values[this_cell]

					for trip_val in trip_set:
						if trip_val in poss_vals:
							poss_vals.remove(trip_val)

					self.check_if_solved(this_cell, poss_vals)



def check_naked_triples_cols(self):
	"""
	for i in range(9):  # i is col number
		self.check_naked_triples_col(i)
	"""
	i = 4

	# print('looking for naked triples in col: {0}'.format(i))
	self.check_naked_triples_col(i)
	# self.solve_queue()


def check_naked_triples_col(self, col_num):
	# Collect candidate cells and their possibilities.
	poss_trip_list = []

	# Get a list of cells that can be part of a triple.
	for j in range(9):
		this_cell = (j, col)

		# Skip over solved cells.
		if this_cell in self.possible_values:
			poss_vals = self.possible_values[this_cell]

			# Can't be part of a triple if there are more than 3 candidates.
			if len(poss_vals) <= 3:
				poss_trip_list.append(this_cell)

	# Analyze if triple exists.
	poss_trips_info = self.find_naked_triples(poss_trip_list)
	self.clean_triple_col(poss_trips_info, col_num)


def clean_triple_col(self, poss_trips_info, col_num):
	# Remove trip possibilities in cells that are not part of the triple.
	for item in poss_trips_info.keys():

		# Decode key and turn it back into a list of numbers.
		trip_set = [int(trip_val) for trip_val in item]
		coords_set = poss_trips_info[item]

		# skip over cells that are part of this triple?
		# remove trip values from cells not part of triple
		for j in range(9):  # j is row number
			this_cell = (j, col_num)















def find_naked_triples(self, poss_trip_list):
	# Make a list of every merged triplet set.
	poss_trips_info = {}  # [trip_str] = [list of coords]
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
			# New possible triplet.
			if trip_str not in poss_trips_info:
				poss_trips_info[trip_str] = trip_coords

				print('cell 1: {0}\tcell 2: {1}\t'.format(cell_1, cell_2), end='')
				print('combined set: {0}'.format(combined_poss))

			# Otherwise, add coords to existing entry.
			else:
				saved_info = poss_trips_info[trip_str]

				for coord in trip_coords:
					if coord not in saved_info:
						saved_info.append(coord)

				poss_trips_info[trip_str] = saved_info


	# look at the dictionary
	"""
	print('what\'s getting passed?')
	for poss_trip in poss_trips_info:
		coords = poss_trips_info[poss_trip]

		print('key: {0}\t\t\t\tval: {1}'.format(poss_trip, coords))
	"""


	# Verify that triples are valid:
	items_to_remove = []
	trips_coords = []

	for poss_trip in poss_trips_info.keys():
		coords_list = poss_trips_info[poss_trip]

		# Length of list: Need 3 coords.
		if len(coords_list) > 3:
			items_to_remove.append(poss_trip)

		# No coord is in more than one trip set.
		for coord in coords_list:
			if coord not in trips_coords:
				trips_coords.append(coord)
			else:
				print('in multiple trip: {0}'.format(coord))



	# Remove invalid triples.
	for item in items_to_remove:
		poss_trips_info.pop(item)


	return poss_trips_info















