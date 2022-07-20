"""
xwing is 2x2.
swordfish is 3x3.
"""


def check_swordfish(self):
	# might eventually turn into the row version of the function

	# lookup table at least three possible locations per row
	swordfish_cands = {}  # for all rows

	for i in range(9):  # i goes down

		val_lookup_row = {}
		for j in range(9):  # j goes across
			this_coord = (i, j)

			# set lookup table
			if this_coord in self.possible_values:
				self.set_lookup_table(this_coord, val_lookup_row)

		# End of row.
		swordfish_cands_row = self.check_swordfish_cands(val_lookup_row)

		for poss_val in swordfish_cands_row.keys():
			if poss_val in swordfish_cands:
				swordfish_cands[poss_val].extend(swordfish_cands_row[poss_val])
			else:
				swordfish_cands[poss_val] = swordfish_cands_row[poss_val]


	# eliminate entries that can't be part of a swordfish
	self.clean_swordfish_list(swordfish_cands)






# #######################################
# General functions
# #######################################
def check_swordfish_cands(self, lookup_dict):
	print('check swordfish cands')
	# eliminate vals with fewer than 3 possible locations
	swordfish_cands = {}

	for poss_val in lookup_dict.keys():
		poss_locs = lookup_dict[poss_val]

		# exactly three or at least three???
		# Add to dict if there are at least 3 possible locations.
		if len(poss_locs) >= 3:
			swordfish_cands[poss_val] = poss_locs

	return swordfish_cands



def clean_swordfish_list(self, swordfish_cands):
	print('clean swordfish list')
	# at least 9 coordinates total, 3 coords in each row
	return None











