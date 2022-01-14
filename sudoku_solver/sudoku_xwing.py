# Import into the main sudoku_solver class.

# When there are
# * only two possible cells for a value in each of two different rows,
# * and these candidates lie also in the same columns,
# then all other candidates for this value in the columns can be eliminated.


def check_xwing(self):

	# for i in [1]:
	for i in range(0, 8):  # i goes down

		val_lookup = {}
		for j in range(0, 8):  # j goes across
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup)


		for poss_val in val_lookup.keys():
			print('{0} - {1}'.format(poss_val, val_lookup[poss_val]))
		print()





def check_xwing_row(self, lookup_dict):
	return None

def xwing_is_same_col(self, coord1, coord2):
	return None











