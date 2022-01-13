# Import into the main sudoku_solver class.



def check_xwing(self):
	val_lookup = {}


	# for i in range(0, 8):  # i goes down
	for i in [1]:
		for j in range(0, 8):  # j goes across
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup)


	for poss_val in val_lookup.keys():
		print('{0} - {1}'.format(poss_val, val_lookup[poss_val]))





def check_xwing_row(self, lookup_dict):
	return None











