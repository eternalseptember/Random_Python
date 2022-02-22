# Import into the main sudoku_solver class.

# When there are
# * only two possible cells for a value in each of two different rows,
# * and these candidates lie also in the same columns,
# then all other candidates for this value in the columns can be eliminated.


def check_xwing(self):
	xwing_candidates = {}  # For all rows.

	# Fill a dict of all possible coord pairs.
	for i in range(0, 8):  # i goes down

		val_lookup_row = {}
		for j in range(0, 8):  # j goes across
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup_row)

		# End of row.
		xwing_cands_row = self.check_xwing_row(val_lookup_row)
		for poss_val in xwing_cands_row.keys():
			if poss_val in xwing_candidates:
				xwing_candidates[poss_val].extend(xwing_cands_row[poss_val])
			else:
				xwing_candidates[poss_val] = xwing_cands_row[poss_val]


	# Eliminate entries that can't be part of an xwing.
	remove_list = []  # store poss_vals
	for poss_val in xwing_candidates.keys():
		poss_coords = xwing_candidates[poss_val]

		# Eliminate the vals with only two possible locations.
		if len(poss_coords) < 3:
			remove_list.append(poss_val)

	# Remove entries that can't be part of an xwing.
	for poss_val in remove_list:
		xwing_candidates.pop(poss_val)


	# Then check each dict entry to see if there's an xwing
	# within the list of coords.
	# can consolidate this into the eliminate entries list later
	xwing_found = {}  # contains a list of four coords

	"""
	for poss_val in xwing_candidates.keys():
		poss_coords = xwing_candidates[poss_val]
		print('{0} - {1}'.format(poss_val, poss_coords))
		self.check_xwing_is_same_cols(poss_val, poss_coords)
	"""

	# smaller test than the section commented out
	poss_val = 7
	poss_coords = xwing_candidates[poss_val]
	xwing_set = self.check_xwing_is_same_cols(poss_val, poss_coords)

	# testing this part
	self.clean_xwing_row(poss_val, xwing_set)


def check_xwing_row(self, lookup_dict):
	# First check this condition:
	# Only two possible cells for a val in each of two different rows.
	xwing_cands_row = {}  # per row

	for poss_val in lookup_dict.keys():
		poss_locs = lookup_dict[poss_val]

		# Add to dict if there are only two possible locations.
		if len(poss_locs) == 2:
			xwing_cands_row[poss_val] = poss_locs

	return xwing_cands_row




def check_xwing_is_same_cols(self, poss_val, list_of_coords):
	print('{0} - {1}\n'.format(poss_val, list_of_coords))

	xwing_set = []  # a list of a set

	# check list_of_coords in groups of two
	# need to account for four coords at a time
	for each_pair_1 in range(0, len(list_of_coords), 2):
		# reference coordinates
		row_1_coord_1 = list_of_coords[each_pair_1]
		row_1_coord_2 = list_of_coords[each_pair_1 + 1]
		row_1_coords = (row_1_coord_1, row_1_coord_2)

		print('{0} {1}:'.format(row_1_coord_1, row_1_coord_2), end=' ')

		# check if there's more coords to compare to
		if (each_pair_1 + 2) >= len(list_of_coords):
			print('no more coords to compare to')
			break


		# rest of coords to compare to
		xwing_row_2_cands = list_of_coords[(each_pair_1 + 2):]
		print('{0}'.format(xwing_row_2_cands))

		for each_pair_2 in range(0, len(xwing_row_2_cands), 2):
			row_2_coord_1 = xwing_row_2_cands[each_pair_2]
			row_2_coord_2 = xwing_row_2_cands[each_pair_2 + 1]
			row_2_coords = (row_2_coord_1, row_2_coord_2)

			is_same_cols = self.is_xwing_same_cols(row_1_coords, row_2_coords)

			print('row 2: {0}, {1}'.format(row_2_coord_1, row_2_coord_2))
			print('is same cols? {0}'.format(is_same_cols))

			if is_same_cols:
				xwing_coords = [row_1_coord_1, row_1_coord_2, row_2_coord_1, row_2_coord_2]
				xwing_set.append(xwing_coords)



	# return a list of four coordinates in the xwing
	print('xwing:')
	for item in xwing_set:
		print(item)

	return xwing_set



def is_xwing_same_cols(self, coords_row_1, coords_row_2):
	# have to check_xwing_row twice for two sets of coordinates
	# coords_row_1 and coords_row_2 are lists.
	coord_1, coord_2 = (coords_row_1)
	coord_3, coord_4 = (coords_row_2)

	row_1, col_1 = (coord_1)
	row_2, col_2 = (coord_2)
	row_3, col_3 = (coord_3)
	row_4, col_4 = (coord_4)

	if (col_1 == col_3) and (col_2 == col_4):
		return True
	else:
		return False



def clean_xwing_row(self, poss_val, coords_list):
	coord_1, coord_2, coord_3, coord_4 = (coords_list)
	return None















