# Import into the main sudoku_solver class.



def check_xwing(self):
	val_lookup = {}

	for i in range(0, 8):  # i goes down
		for j in range(0, 8):  # j goes across
			this_coord = (i, j)
			self.set_lookup_table(this_coord, val_lookup)

			print('coord: {0}'.format(this_coord))
			for poss_val in val_lookup.keys():
				print('{0} - {1}'.format(poss_val, val_lookup[poss_val]))
			print()




def set_lookup_table_row(self, row_num):
	return None











