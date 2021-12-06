# Import into the main sudoku_solver class.
"""
Naked triple:
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""


def check_naked_triples(self):
	# self.check_naked_triples_rows()
	self.check_naked_triples_cols()




def check_naked_triples_rows(self):
	# Iterate through each row to find naked triples.
	for j in range(9):  # j is row number
		self.check_naked_triples_row(j)

	# j = 0
	# self.check_naked_triples_row(j)

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
	"""
	for i in range(9):  # i is col number
		self.check_naked_triples_col(i)
	"""

	i = 0
	self.check_naked_triples_col(i)

	# self.solve_queue()


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
	# self.clean_triple_col(poss_trips_info, col_num)


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
	# Make a list of every possible merged triplet set.
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

			# Otherwise, add coord to existing triplet.
			else:
				saved_info = poss_trips_info[trip_str]

				for coord in trip_coords:
					if coord not in saved_info:
						saved_info.append(coord)

				poss_trips_info[trip_str] = saved_info

	return self.verify_triples_list(poss_trips_info)



def verify_triples_list(self, poss_trips_info):
	# Remove entries from poss_trips_info if triple is not valid.
	entries_to_remove = []  # List of str keys.

	# List of vals and coords in possible triplets.
	# Used for finding vals and coords in multiple possible trips.
	trips_coords = []
	trips_vals = []

	# Used for finding the first set for removal.
	coords_in_mult_trips = []
	vals_in_mult_trips = []

	# First pass at cleaning up poss_trips_info.
	for trip_str in poss_trips_info.keys():
		coords_list = poss_trips_info[trip_str]
		trip_vals_list = list(map(int, trip_str))  # converted to list

		# Length of list: Need 3 coords.
		if len(coords_list) != 3:
			entries_to_remove.append(trip_str)

		# No coord is in more than one trip set.
		for coord in coords_list:
			if coord not in trips_coords:
				trips_coords.append(coord)
			else:
				# print('coord in multiple trip: {0}'.format(coord))
				entries_to_remove.append(trip_str)

				# For finding the first occurance to remove.
				coords_in_mult_trips.append(coord)


		# No possible value is in more than one trip set.
		for trip_val in trip_vals_list:
			if trip_val not in trips_vals:
				trips_vals.append(trip_val)
			else:
				# print('val in multiple trip: {0}'.format(trip_val))
				entries_to_remove.append(trip_str)

				# For finding the first occurance to remove.
				vals_in_mult_trips.append(trip_val)


	# Search through the list for the FIRST occurance.
	# Remove from triplet consideration: coords and vals in multiple trips.
	if len(coords_in_mult_trips) > 0:
		for entry in poss_trips_info.keys():
			coords_list = poss_trips_info[entry]

			# Check if coord is in multiple trips here.
			for coord in coords_in_mult_trips:
				if coord in coords_list:
					entries_to_remove.append(entry)

					# Once entry has been added to entries_to_remove,
					# break to next entry.
					break


	if len(vals_in_mult_trips) > 0:
		# get coordinates and put them in entries_to_remove
		for trip_str in poss_trips_info.keys():
			trip_vals_list = list(map(int, trip_str))  # convert

			# Check if val is in multiple trips here.
			for val in vals_in_mult_trips:
				if val in trip_vals_list:
					entries_to_remove.append(trip_str)

					# Once trip_str has been added to entries_to_remove,
					# break to next trip_str.
					break


	# Remove duplicates first, then remove triplet candidates.
	entries_to_remove = list(set(entries_to_remove))
	for item in entries_to_remove:
		poss_trips_info.pop(item)


	# Triples have been verified. Check if they're in the same box.
	self.check_naked_triples_box(poss_trips_info)


	return poss_trips_info








def check_naked_triples_box(self, poss_trips_info):
	# poss_trips_info[trip_str] = [list of coords]
	triple_boxes = []  # store trip_str if coords are in the same box


	print('checking naked triples box')
	for trip_vals in poss_trips_info.keys():
		trip_coords = poss_trips_info[trip_vals]
		# print('{0}: {1}'.format(trip_vals, trip_coords))

		box_row = None
		box_col = None
		same_box = True

		for coord in trip_coords:
			this_row, this_col = (coord)
			print('box row: {0}\tbox col:{1}'.format(this_row, this_col))

			# set row and col if they're unset
			# compare if they match
			if box_row is None:
				box_row = this_row
			elif box_row != this_row:
				same_box = False
				break  # go to the next trip_vals

			if box_col is None: 
				box_col = this_col
			elif box_col != this_col:
				same_box = False
				break  # go to the next trip_vals


		if same_box:
			triple_boxes.append(trip_coords)

	# if there are any triples inside a box, clean the box.
	if len(triple_boxes) > 0:
		print()






def clean_triple_box(self, poss_trips_info, trip_box_info):
	return None




















