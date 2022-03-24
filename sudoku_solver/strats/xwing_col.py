# Starts xwing check by looking for candidates in each *col*.

# When there are
# * only two possible cells for a value in each of two different cols,
# * and these candidates lie also in the same rows,
# then all other candidates for this value in the rows can be eliminated.



def check_xwing_cols(self):
	xwing_candidates = {}  # For all cols.

	# Fill a dict of all possible coord pairs.
	for j in range(0, 8):  # j goes across

		val_lookup_row = {}
		for i in range(0, 8):  # i goes down
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup_row)





def check_xwing_is_same_rows(self, lookup_dict):
	xwing_set = []  # a list of a set



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

















