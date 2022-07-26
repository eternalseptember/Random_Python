"""
xwing is 2x2.
swordfish is 3x3.
"""


def check_swordfish(self):
	# Row and col versions not necessary.

	# First, fill a dict of all possible coord pairs.
	swordfish_cands = {}  # for all rows

	for i in range(9):  # i goes down

		val_lookup_row = {}
		for j in range(9):  # j goes across
			this_coord = (i, j)

			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup_row)

		# End of row.
		self.check_swordfish_cands(val_lookup_row)

		for poss_val in val_lookup_row.keys():
			if poss_val in swordfish_cands:
				swordfish_cands[poss_val].extend(val_lookup_row[poss_val])
			else:
				swordfish_cands[poss_val] = val_lookup_row[poss_val]


	# Eliminate poss_vals that can't be part of a swordfish.
	self.clean_swordfish_list(swordfish_cands)






# #######################################
# General swordfish functions
# #######################################
def check_swordfish_cands(self, lookup_dict):
	# Conditions: at least 3 possible locations per row.
	remove_list = []

	for poss_val in lookup_dict.keys():
		poss_locs = lookup_dict[poss_val]

		# Check conditions.
		if len(poss_locs) <= 2:
			remove_list.append(poss_val)

	# Remove entries.
	for poss_val in remove_list:
		lookup_dict.pop(poss_val)




def clean_swordfish_list(self, swordfish_cands):
	# Conditions: at least 9 coordinates total; 3 coords in each col.
	remove_list = []  # store poss_vals

	# Check conditions.
	for poss_val in swordfish_cands.keys():
		poss_coords = swordfish_cands[poss_val]

		if len(poss_coords) <= 9:
			remove_list.append(poss_val)

	# Remove entries.
		for poss_val in remove_list:
		swordfish_cands.pop(poss_val)

















