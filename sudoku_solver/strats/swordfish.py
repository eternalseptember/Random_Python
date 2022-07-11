"""
xwing is 2x2.
swordfish is 3x3.
"""


def check_swordfish(self):
	# lookup table at least three possible locations per row

	for i in range(9):  # i goes down

		val_lookup_row = {}
		for j in range(9):  # j goes across
			this_coord = (i, j)

			# set lookup table
			# but eliminate vals with fewer than 3 possible locations
			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup_row)






def check_swordfish_cands(self, lookup_dict):
	return None




