# Functions that eliminate possibilities based on matching pairs or triplets.
# Import into the main sudoku_solver class.


def check_matching_sets(self):
	# Run this if checking unique doesn't solve everything.
	"""
	elimination due to matching pairs will get both examples.
	are missing values all in the same box?

	tally each row/col's missing values.
	In puzzle_5:
	column 6 is missing 4 and 6, which are in the same box.
	Remove possibilities outside this col within this box (0-2, 7),
	because col is mostly solved, but box is not.


	tally each box's missing values.
	In puzzle_5:
	the missing values of the central box are in the same col, so remove
	6 and 9 as possiblities outside the box in the same column (row, 4).
	Remove possibilities from same col outside of this box,
	because box is mostly solved, but col is not.


	1. remove from row or col first.
	2. then if values share the same box, remove from the rest of the box.
	"""
	self.check_matching_cols()
	# self.check_matching_rows()



def check_matching_cols(self):
	# Search each col for matching pairs/triplets.
	for col in range(9):
		col_missing_vals = {}

		# Collect all the missing value combinations in this col.
		for j in range(9):  # j goes down
			this_cell = (j, col)
			self.set_missing_val_table(this_cell, col_missing_vals)

		# Search this col's tally for pair/triplet matches.
		matches = self.find_matches(col_missing_vals)

		# If there are matching sets, remove values as possibilities in other
		# boxes outside the set/pair/triplet.
		if len(matches) > 0:
			for match in matches:
				# Col
				print('Reduce in col.')
				for j in range(9):  # j goes down
					this_cell = (j, col)
					self.remove_matching_sets(this_cell, match)

				# Box
				print('Reduce in box.')
				# check whether all values in match are in the same box
				self.in_same_box(match)

			# If anything's been reduced to one possibility:
			self.solve_queue()


def check_matching_rows(self):
	# search each row for pairs/triplets
	for row in range(9):
		row_missing_values = {}

		for i in range(9):  # i goes across
			this_cell = (row, i)


def set_missing_val_table(self, coord, missing_val_dict):
	# Tallies the combinations of missing values in each area.
	if coord in self.possible_values:
		poss_values = self.possible_values[coord]

		# Convert to hashable key.
		poss_str = ''.join(map(str, poss_values))

		# Tally combinations of missing values.
		if poss_str in missing_val_dict:
			missing_val_dict[poss_str] += 1
		else:
			missing_val_dict[poss_str] = 1


def find_matches(self, missing_val_dict):
	# Search the dictionary of missing values for matches between
	# possible values in a cell and
	# the number of cells with that exact list of possibilities.
	matches = []

	for missing_val in missing_val_dict.keys():
		if len(missing_val) == missing_val_dict[missing_val]:
			# Turn missing_val hash back into a list.
			missing_val_list = [int(val) for val in missing_val]
			matches.append(missing_val_list)

	return matches


def in_same_box(self, matched_set):
	# matched_set is a list of values in the pair/triplet/set.
	return


def remove_matching_sets(self, coord, matched_set):
	# matched_set is a list of values in the pair/triplet/set.
	if coord in self.possible_values:
		poss_values = self.possible_values[coord]

		if poss_values == matched_set:
			# Don't want to erase the match.
			print('Matches found: {0} at {1}'.format(matched_set, coord))
			return
		else:
			# Remove any values in the matched set.
			for val in matched_set:
				if val in poss_values:
					poss_values.remove(val)

			# Check if solved.
			if len(poss_values) == 1:
				if (coord not in self.solved_list) and \
					(coord not in self.solved_queue):
					self.solved_queue.append(coord)















