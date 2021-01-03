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
	# Within each 3x3 box, tally up whether unfilled values fit within row.
	# If so, then eliminate them as possibilities from neighboring boxes.

	# keys: hashable string; value: dict containing info about missing vals
	block_col_info = {}  # subdict keys: "num_missing", "in_cols", "in_boxes"

	for i in [0, 3, 6]:  # i goes down.
		block_row_info = {}  # subdict keys: "num_missing", "in_rows", "in_boxes"

		for j in [0, 3, 6]:  # j goes across.
			coord = (i, j)

			# rows_list, cols_list = self.check_within_a_box(coord)
			self.check_within_a_box(coord)

			# Process info for block-row analysis.
			# Create a hashable key out of the info given.
			"""
			for missing_val in rows_list.keys():
				rows_str = ''
				rows_str += '{0}-'.format(missing_val)
				rows_str += ''.join(map(str, rows_list[missing_val]))

				# Info about missing values.
				if rows_str not in block_row_info:
					block_row_info[rows_str] = {
						'num_missing': missing_val,
						'in_rows': rows_list[missing_val],
						'in_boxes': [j]
						}
				else:
					row_info = block_row_info[rows_str]
					row_info['in_boxes'].append(j)
			"""


			# process info for block-col analysis.
			# Create a hashable key out of the info given.
			"""
			for missing_val in cols_list.keys():
				cols_str = ''
				cols_str += '{0}-'.format(missing_val)
				cols_str += ''.join(map(str, cols_list[missing_val]))

				# info about missing values
				if cols_str not in block_col_info:
					block_col_info[cols_str] = {
						'num_missing': missing_val,
						'in_cols': cols_list[missing_val],
						'in_boxes': [i]  # ??????
					}
				else:
					col_info = block_col_info[cols_str]
					col_info['in_boxes'].append(i)
				"""


		# Eliminate possibilities in this row's third box.
		"""
		print('third box possiblities')
		for str_key in rows_list.keys():
			print('key: {0}'.format(str_key))
			print('\t{0}'.format(rows_list[str_key]))
		"""
		# print('eliminate possibilities in third box of ROW')
		# self.remove_rows_in_box(block_row_info)


	# Eliminate possibilities in each col's third box.
	# print('eliminate possibilities in third box of COL')
	# self.remove_cols_in_box(block_col_info)

	self.solve_queue()  # Not sure if this goes here.




def check_within_a_box(self, coord):
	# coord defines the 3x3 box.
	# Check within a single box to see whether missing values can be narrowed
	# down to specific rows.
	"""
	rows_list = {}
	cols_list = {}
	"""

	# Get the list of missing values and their possible locations in this box.
	poss_vals_in_box = self.get_box_poss_vals(coord)

	# For each missing value, analyze the list of their possible locations.
	for missing_val in poss_vals_in_box.keys():
		poss_locs_list = poss_vals_in_box[missing_val]

		# Are they in the same row?
		in_rows_list = self.in_which_rows(poss_locs_list)

		# If missing_val can only be in one row within this box, then remove
		# missing_val as possibilities in the rest of the row outside this box.
		if len(in_rows_list) == 1:
			self.remove_row_outside_box(missing_val, coord, in_rows_list[0])
		"""
		# Otherwise, collect info for block-level analysis.
		elif len(in_rows_list) == 2:
			rows_list[missing_val] = in_rows_list
		"""

		# Are they in the same col?
		in_cols_list = self.in_which_cols(poss_locs_list)

		# If missing_val can only be in one col within this box, then remove
		# missing_val as possibilities in the rest of the col outside this box.
		if len(set(in_cols_list)) == 1:
			self.remove_col_outside_box(missing_val, coord, in_cols_list[0])
		"""
		# Otherwise, collect info for block-level analysis.
		elif len(in_cols_list) == 2:
			cols_list[missing_val] = in_cols_list
		"""

	# Returns info for each individual 3x3 box.
	# Use it to establish what needs to be eliminated in the remaining box.
	# return rows_list, cols_list


def in_which_rows(self, coords_list):
	# Which rows could the cells be in?
	rows = []

	# Unpack and tally rows here.
	for coord in coords_list:
		row, col = coord
		rows.append(row)

	# Not useful if it returns 3.
	return list(set(rows))


def in_which_cols(self, coords_list):
	# Which cols could the cells be in?
	cols = []

	# Unpack and tally cols here.
	for coord in coords_list:
		row, col = coord
		cols.append(col)

	# Not useful if it returns 3.
	return list(set(cols))


def remove_row_outside_box(self, eliminated_val, ref_box, in_row):
	# eliminated_val is the value to be removed.
	# ref_box defines the 3x3 box.
	ref_row, ref_col = ref_box
	box_col = ref_col // 3  # Remove in row outside this box.

	for i in range(9):  # i goes across.
		# Skip the box with coord.
		if i // 3 == box_col:
			continue

		# Remove eliminated_val as a possible val in this cell.
		this_cell = (in_row, i)
		self.possible_vals_check(this_cell, eliminated_val)


def remove_col_outside_box(self, eliminated_val, ref_box, in_col):
	# eliminated_val is the value to be removed.
	# ref_box defines the 3x3 box.
	ref_row, ref_col = ref_box
	box_row = ref_row // 3  # Remove in col outside this box.

	for j in range(9):  # j goes down.
		# Skip the box with coord.
		if j // 3 == box_row:
			continue

		# Remove eliminated_val as a possible val in this cell.
		this_cell = (j, in_col)
		self.possible_vals_check(this_cell, eliminated_val)



def remove_rows_in_box(self, block_info):
	# Given info about a missing value and which two rows of which two boxes
	# they're in, remove those possibilities in the third box.

	# Unpack block_info.
	# Key for dict on missing vals in two boxes, leading to eliminating
	# those missing vals as possibilities in third box.
	for block_key in block_info.keys():
		box_info = block_info[block_key]  # value is a dict

		num_missing = box_info['num_missing']
		in_rows = box_info['in_rows']
		in_boxes = box_info['in_boxes']

		# Figure out the box to remove info from.
		box_remaining = [0, 3, 6]
		for box in in_boxes:
			box_remaining.remove(box)
		box_remaining = box_remaining[0]

		print('num: {0} in rows: {1} in box: {2}'
			.format(num_missing, in_rows, box_remaining))

		# Remove num_missing.
		for i in range(3):
			this_col = i + box_remaining

			for elim_val_in_this_row in in_rows:
				this_coord = (elim_val_in_this_row, this_col)
				self.possible_vals_check(this_coord, num_missing)



def remove_cols_in_box(self, block_info):
	# Given info about a missing value and which two cols of which two boxes
	# they're in, remove those possibilities in the third box.

	# Unpack block_info.
	# Key for dict on missing vals in two boxes, leading to eliminating
	# those missing vals as possibilities in third box.
	for block_key in block_info.keys():
		box_info = block_info[block_key]  # value is a dict

		num_missing = box_info['num_missing']
		in_cols = box_info['in_cols']
		in_boxes = box_info['in_boxes']

		# Figure out the box to remove info from.
		box_remaining = [0, 3, 6]
		for box in in_boxes:
			box_remaining.remove(box)
		box_remaining = box_remaining[0]

		print('num: {0} in box: {1} in cols: {2}'
			.format(num_missing, box_remaining, in_cols))

		# Remove num_missing.
		for j in range(3):
			this_row = j + box_remaining  # ?

			for elim_val_in_this_col in in_cols:
				this_coord = (this_row, elim_val_in_this_col)
				self.possible_vals_check(this_coord, num_missing)


def check_block_elim(self):
	# Check all nine boxes for patterns to eliminate possibilities.
	# Within each 3x3 box, 
	# tally up whether unfilled values fit within the same two rows.
	# Then check neighboring boxes.
	# By the process of elimination,
	# deduce where that number is in the third row.

	# keys: hashable string; value: dict containing info about missing vals
	# subdict keys: "num_missing", "in_cols", "in_boxes"
	block_col_info = {}  # pre-hashed?

	for i in [0, 3, 6]:  # i goes down.
		block_row_info = {}  # subdict keys: "num_missing", "in_rows", "in_boxes"

		for j in [0, 3, 6]:  # j goes across.
			coord = (i, j)

			# Get list of missing vals and their poss locs in this box.
			poss_vals_in_box = self.get_box_poss_vals(coord)

			# For each missing val, get list of their possible locations.
			for missing_val in poss_vals_in_box.keys():
				poss_locs_list = poss_vals_in_box[missing_val]

				# are they in the same rows or cols?
				in_rows_list = self.in_which_rows(poss_locs_list)
				in_cols_list = self.in_which_cols(poss_locs_list)

				if len(in_rows_list) == 2:
					block_row_info[missing_val] = in_rows_list
					# print('scanning at coord {0}\tmissing val: {1}\tin rows: {2}'.format(coord, missing_val, in_rows_list))

					# create a hashable key
					rows_str = '{0}-'.format(missing_val)
					rows_str += ''.join(map(str, in_rows_list))
					# print('hash string: {0}'.format(rows_str))

					if rows_str not in block_row_info:
						block_row_info[rows_str] = {
							'num_missing': missing_val,
							'in_rows': in_rows_list,
							'in_boxes': [j]
						}
					else:
						row_info = block_row_info[rows_str]
						row_info['in_boxes'].append(j)



				"""
				if len(in_cols_list) == 2:
					print('do more stuff here')
				"""




















