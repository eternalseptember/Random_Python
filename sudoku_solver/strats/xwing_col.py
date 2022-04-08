# Starts xwing check by looking for candidates in each *col*.

# When there are
# * only two possible cells for a value in each of two different cols,
# * and these candidates lie also in the same rows,
# then all other candidates for this value in the rows can be eliminated.



def check_xwing_cols(self):
	xwing_candidates = {}  # For all cols.

	# Fill a dict of all possible coord pairs.
	for j in range(0, 8):  # j goes across

		val_lookup_col = {}
		for i in range(0, 8):  # i goes down
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup_col)

		# End of col.
		xwing_cands_col = self.check_xwing_cands(val_lookup_col)
		for poss_val in xwing_cands_col.keys():
			if poss_val in xwing_candidates:
				xwing_candidates[poss_val].extend(xwing_cands_col[poss_val])
			else:
				xwing_candidates[poss_val] = xwing_cands_col[poss_val]


	# Eliminate entries that can't be part of an xwing.
	self.clean_xwing_list(xwing_candidates)


	print('cleaned xwing list:')
	for poss_val in xwing_candidates.keys():
		print('{0} - {1}'.format(poss_val, xwing_candidates[poss_val]))



	"""
	for poss_val in xwing_candidates.keys():
		poss_coords = xwing_candidates[poss_val]
		xwing_set = self.check_xwing_is_same_rows(poss_val, poss_coords)


	if len(xwing_set) == 0:
		return None
	else:
		self.clean_xwing_row(poss_val, xwing_set)
	"""




def check_xwing_is_same_rows(self, poss_val, list_of_coords):
	print('{0} - {1}\n'.format(poss_val, list_of_coords))

	xwing_set = []  # a list of a set


	# is this right?
	for each_pair_1 in range(0, len(list_of_coords), 2):
		col_1_coord_1 = list_of_coords[each_pair_1]
		col_1_coord_2 = list_of_coords[each_pair_1 + 1]





def is_xwing_same_rows(self, coords_col_1, coords_col_2):
	# coords_col_1 and coords_col_2 are lists.
	coord_1, coord_2 = (coords_col_1)
	coord_3, coord_4 = (coords_col_2)

	row_1, col_1 = (coord_1)
	row_2, col_2 = (coord_2)
	row_3, col_3 = (coord_3)
	row_4, col_4 = (coord_4)

	# maybe???
	if (row_1 == row_3) and (row_2 == row_4):
		return True
	else:
		return False






def clean_xwing_row(self, poss_val, coords_list):
	# coords in coords_list is listed in a specific order
	coord_1 = coords_list[0]
	coord_2 = coords_list[1]
	coord_3 = coords_list[2]
	coord_4 = coords_list[3]

	row_1, col_1 = (coord_1)
	row_2, col_2 = (coord_2)
	row_3, col_3 = (coord_3)
	row_4, col_4 = (coord_4)

	# maybe???
	clean_row_1 = row_1
	clean_row_2 = row_2

















