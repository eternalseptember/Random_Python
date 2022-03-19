# Starts xwing check by looking for candidates in each *col*.

# When there are
# * only two possible cells for a value in each of two different cols,
# * and these candidates lie also in the same rows,
# then all other candidates for this value in the rows can be eliminated.



def check_xwing_cols(self):
	xwing_candidates = {}  # For all cols.



def check_xwing_col(self):
	xwing_cands_col = {}  # per col



def check_xwing_is_same_rows(self, lookup_dict):
	xwing_set = []  # a list of a set



def is_xwing_same_rows(self, coords_col_1, coords_col_2):
	# coords_col_1 and coords_col_2 are lists.
	coord_1, coord_2 = (coords_col_1)
	coord_3, coord_4 = (coords_col_2)



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

















