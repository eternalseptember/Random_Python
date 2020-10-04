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
			self.check_within_box(coord)


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
	rows = []

	# Unpack and tally rows here.
	for coord in coords_list:
		row, col = coord
		rows.append(row)

	# Are they all in the same row?
	# And if they are, which row?
	if len(set(rows)) == 1:
		return True, rows[0]
	else:
		return False, None


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
		poss_values = self.possible_values[this_cell]

		if eliminated_val in poss_values:
			poss_values.remove(eliminated_val)



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
		poss_values = self.possible_values[this_cell]

		if eliminated_val in poss_values:
			poss_values.remove(eliminated_val)


def block_interaction(self):
	# block_elim
	print()










