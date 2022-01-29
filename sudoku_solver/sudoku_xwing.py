# Import into the main sudoku_solver class.

# When there are
# * only two possible cells for a value in each of two different rows,
# * and these candidates lie also in the same columns,
# then all other candidates for this value in the columns can be eliminated.


def check_xwing(self):
	xwing_candidates = {}  # for all rows

	# for i in [1]:
	for i in range(0, 8):  # i goes down

		val_lookup = {}
		for j in range(0, 8):  # j goes across
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup)


		# end of row
		xwing_cands_row = self.check_xwing_row(val_lookup)
		# how to append to xwing_candidates
		for poss_val in xwing_cands_row.keys():
			if poss_val in xwing_candidates:
				# ???
				xwing_candidates[poss_val].extend(xwing_cands_row[poss_val])
			else:
				xwing_candidates[poss_val] = xwing_cands_row[poss_val]

	# print dictionary for testing
	for poss_val in xwing_candidates.keys():
		poss_coords = xwing_candidates[poss_val]
		print('{0}: {1}'.format(poss_val, poss_coords))





def check_xwing_row(self, lookup_dict):
	# first check this condition:
	# only two possible cells for a value in each of two different rows
	xwing_cands_row = {}  # per row

	for poss_val in lookup_dict.keys():
		poss_locs = lookup_dict[poss_val]

		# add to dict if there are only two possible locations
		if len(poss_locs) == 2:
			xwing_cands_row[poss_val] = poss_locs
			# print('{0} - {1}'.format(poss_val, poss_locs))

	return xwing_cands_row




def xwing_is_same_cols(self, list_of_coords):
	# check list_of_coords in groups of two
	return None



"""
def xwing_is_same_cols(self, coords_row_1, coords_row_2):
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
"""










