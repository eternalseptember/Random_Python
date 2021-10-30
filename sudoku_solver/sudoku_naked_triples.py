# Import into the main sudoku_solver class.
"""
Naked triple:
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""


def check_naked_triples(self):
	self.check_naked_triples_rows()
	# self.check_naked_triples_cols()


def check_naked_triples_rows(self):
	# Iterate through each row to find naked triples.

	"""
	for j in range(9):  # j is row number
		self.check_naked_triples_row(j)
	"""

	# j = 4
	j = 0
	self.check_naked_triples_row(j)

	self.print_possible_values()
	print('something in solved queue? {0}'.format(len(self.solved_queue)))

	self.solve_queue()



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

		# Remove trip values from cells not part of triple.
		for i in range(9):  # i is col number
			this_cell = (row_num, i)

			# Skip over cells that are part of this triple.
			if this_cell not in coords_set:
				if this_cell in self.possible_values:

					# Remove vals in trip_set from this cell's possible vals.
					poss_vals = self.possible_values[this_cell]

					for trip_val in trip_set:
						if trip_val in poss_vals:
							poss_vals.remove(trip_val)

					self.check_if_solved(this_cell, poss_vals)









def check_naked_triples_cols(self):
	# Iterate through each col to find naked triples.
	for i in range(9):  # i is col number
		self.check_naked_triples_col(i)

	# i = 4
	# self.check_naked_triples_col(i)

	self.solve_queue()  # error here


def check_naked_triples_col(self, col_num):
	# Collect candidate cells and their possibilities.
	poss_trip_list = []

	# Get a list of cells that can be part of a triple.
	for j in range(9):
		this_cell = (j, col_num)

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

		# Remove trip values from cells not part of triple.
		for j in range(9):  # j is row number
			this_cell = (j, col_num)

			# Skip over cells that are part of this triple.
			if this_cell not in coords_set:
				if this_cell in self.possible_values:
					poss_vals = self.possible_values[this_cell]

					# Remove vals in trip_set from this cell's possible vals.
					poss_vals = self.possible_values[this_cell]

					for trip_val in trip_set:
						if trip_val in poss_vals:
							poss_vals.remove(trip_val)

					self.check_if_solved(this_cell, poss_vals)









def find_naked_triples(self, poss_trip_list):
	#
	# Make a list of every merged triplet set.
	#
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

		# Two cells combined and have fewer than 3 possible combinations are
		# taken care by other functions.
		if len(combined_poss) <= 3:
			# New possible triplet.
			if trip_str not in poss_trips_info:
				poss_trips_info[trip_str] = trip_coords

				print('cell 1: {0}\tcell 2: {1}\t'.format(cell_1, cell_2), end='')
				print('combined set: {0}'.format(combined_poss))

			# Otherwise, add coord to existing triplet.
			else:
				saved_info = poss_trips_info[trip_str]

				for coord in trip_coords:
					if coord not in saved_info:
						saved_info.append(coord)

				poss_trips_info[trip_str] = saved_info


	#
	# Verify that triples are valid.
	#
	coords_to_remove = []
	trips_coords = []  # For finding coords in multiple possible trips.
	trips_vals = []  # For finding vals in multiple possible trips.
	coords_in_mult_trips = []  # Remove these coords.
	vals_in_mult_trips = []  # Remove these vals.

	for trip_str in poss_trips_info.keys():
		coords_list = poss_trips_info[trip_str]

		# Length of list: Need 3 coords.
		if len(coords_list) > 3:
			coords_to_remove.append(trip_str)

		# No coord is in more than one trip set.
		for coord in coords_list:
			if coord not in trips_coords:
				trips_coords.append(coord)
			else:
				print('in multiple trip: {0}'.format(coord))
				coords_in_mult_trips.append(coord)

		# No possible value is in more than one trip set.
		this_trip_vals = list(map(int, trip_str))  # convert

		for trip_val in this_trip_vals:
			if trip_val not in trips_vals:
				trips_vals.append(trip_val)
			else:
				print('in multiple trip: {0}'.format(trip_val))
				vals_in_mult_trips.append(trip_val)

				# add the coords that has vals in multiple trips
				for coord in coords_list:
					if coord not in trips_coords:
						trips_coords.append(coord)



	# Remove from triplet consideration: coords in multiple trips.
	if len(coords_in_mult_trips) > 0:
		for entry in poss_trips_info.keys():
			coords_list = poss_trips_info[entry]

			# check for multiple trips here
			for coord in coords_in_mult_trips:
				if coord in coords_list:
					coords_to_remove.append(entry)

					# Once entry has been added to coords_to_remove,
					# break to new entry.
					break


	# search through the list for the first occurance
	if len(vals_in_mult_trips) > 0:
		# get coordinates and put them in coords_to_remove
		for trip_str in poss_trips_info.keys():
			this_trip_vals = list(map(int, trip_str))  # convert








	# Remove invalid triples.
	for item in coords_to_remove:
		# check what's getting removed?
		# print('item being removed: {0}'.format(item))
		poss_trips_info.pop(item)

	"""
	print('poss trips info')
	for item in poss_trips_info.keys():
		print('{0}: {1}'.format(item, poss_trips_info[item]))
	"""

	return poss_trips_info















