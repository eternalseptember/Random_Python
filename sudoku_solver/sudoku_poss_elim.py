# Functions that eliminate possibilities based on row/box/col interactions.
# Import into the main sudoku_solver class.

"""
In puzzle_5:
the missing values of the central box are in the same col, so remove
6 and 9 as possiblities outside the box in the same column (row, 4).
Remove possibilities from same col outside of this box,
because box is mostly solved, but col is not.
"""


def check_within_boxes(self):
	# Check all nine boxes for patterns to eliminate possibilities.
	for i in [0, 3, 6]:
		for j in [0, 3, 6]:
			coord = (i, j)
			self.check_within_a_box(coord)


def check_within_a_box(self, coord):
	# Check within a single box to eliminate possibilities.
	# coord defines the 3x3 box.
	"""
	Example: If a box is missing the value 7, and the only possible locations
	for 7 are in the same row, then remove 7 as possibilities in the rest of
	the row outside the box.
	"""

	# Get the list of missing values and their possible locations in this box.
	poss_vals_in_box = self.get_box_poss_vals(coord)

	# For each missing value, analyze the list of their possible locations.
	for missing_val in poss_vals_in_box.keys():
		poss_locs_list = poss_vals_in_box[missing_val]

		# Are they in the same row or col?
		is_same_row, row_num = self.in_same_row(poss_locs_list)
		is_same_col, col_num = self.in_same_col(poss_locs_list)

		# Remove missing_val.
		if is_same_row:
			self.remove_in_row_outside_box(missing_val, coord)
		if is_same_col:
			self.remove_in_col_outside_box(missing_val, coord)


def in_same_row(self, coords_list):
	# Are all the cells in coords_list in the same row?
	rows_list = self.in_which_rows(coords_list)

	# Are they all in the same row?
	# And if they are, which row?
	if len(rows_list) == 1:

		print('rows_list:', end=' ')
		print(rows_list)

		return True, rows_list[0]
	else:
		return False, None


def in_which_rows(self, coords_list):
	# Which rows could the cells be in?
	rows = []

	# Unpack and tally rows here.
	for coord in coords_list:
		row, col = coord
		rows.append(row)

	# Not useful if it returns 3.
	return list(set(rows))


def in_same_col(self, coords_list):
	# Are all the cells in coords_list in the same row?
	cols = []

	# Unpack and tally cols here.
	for coord in coords_list:
		row, col = coord
		cols.append(col)

	# Are they all in the same col?
	# And if they are, which col?
	if len(set(cols)) == 1:
		return True, cols[0]
	else:
		return False, None





def in_which_cols(self, coords_list):
	print()





def remove_in_row_outside_box(self, eliminated_val, coord):
	# eliminated_val is the value to be removed
	# coord defines the 3x3 box.
	ref_row, ref_col = coord
	box_col = ref_col // 3  # Box coord is in.

	for i in range(9):  # i goes across
		# Skip the box with coord.
		if i // 3 == box_col:
			continue

		# Remove eliminated_val as a possible val in this cell.
		this_cell = (ref_row, i)

		if this_cell in self.possible_values:
			poss_values = self.possible_values[this_cell]

			if eliminated_val in poss_values:
				poss_values.remove(eliminated_val)

			# #################################################################
			# REMEMBER TO CHECK IF THERE'S ONLY ONE VALUE LEFT
			# AND ADD TO SOLVED_QUEUE
			# #################################################################



def remove_in_col_outside_box(self, eliminated_val, coord):
	# eliminated_val is the value to be removed
	# coord defines the 3x3 box.
	ref_row, ref_col = coord
	box_row = ref_row // 3  # Box coord is in.

	for j in range(9):  # j goes across
		# Skip the box with coord.
		if j // 3 == box_row:
			continue

		# Remove eliminated_val as a possible val in this cell.
		this_cell = (j, ref_col)

		if this_cell in self.possible_values:
			poss_values = self.possible_values[this_cell]

			if eliminated_val in poss_values:
				poss_values.remove(eliminated_val)

			# #################################################################
			# REMEMBER TO CHECK IF THERE'S ONLY ONE VALUE LEFT
			# AND ADD TO SOLVED_QUEUE
			# #################################################################


# =============================================================================

# Add these functions to the main sudoku_solver page.

def check_block_level_elim(self):
	# known info from two sets of 3x3 box, what does it mean for the third 3x3 box
	# in the same board-level row or col?
	print()


def check_block_row(self):
	"""
	within each 3x3 box,
	tally up whether unfilled values fit within the same rows.
	then check with neighboring boxes.
	by the process of elimination, deduce where that number is in the third row
	"""

	# these are not final values. testing function.
	# perhaps collect all of these in the function that would run this.

	for box_col in [0, 3, 6]:  # checking a row means row is constant.
		coord = (3, box_col)
		self.check_box_row_elim((coord))



def check_block_col(self):
	print()


def check_box_row_elim(self, coord):
	# coord defines the 3x3 box.
	# Check within a single box to see whether missing values can be narrowed
	# down to specific rows.
	# could merge with check_within_a_box function
	rows_list = {}

	# Get the list of missing values and their possible locations in this box.
	poss_vals_in_box = self.get_box_poss_vals(coord)

	# For each missing value, analyze the list of their possible locations.
	for missing_val in poss_vals_in_box.keys():
		poss_locs_list = poss_vals_in_box[missing_val]

		# check which rows they are in

		# REDO THIS PART
		in_rows_list = self.in_which_rows(poss_locs_list)

		if len(in_rows_list) < 3:
			rows_list[missing_val] = in_rows_list

			print('missing value: {0} in'.format(missing_val), end=' ')
			print(in_rows_list)



def check_box_col_elim(self, coord):
	print()























