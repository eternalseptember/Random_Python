# Similar to naked subset.
# Import into the main sudoku_solver class.


def check_hidden_subsets(self):
	return None


def check_hidden_sub_col(self):
	# ... NOT SURE I UNDERSTAND CONCEPTUALLY ...

	col_missing_vals = {}  # get list of missing values of this col
	col = 0  # manually setting for now

	for j in range(9):  # row goes down, col is constant
		this_cell = (j, col)
		# self.set_missing_val_table(this_cell, col_missing_vals)
		if this_cell in self.possible_values:
			print('{0}: {1}'.format(this_cell, self.possible_values[this_cell]))


	"""
	for info in col_missing_vals.keys():
		print('{0}: {1}'.format(info, col_missing_vals[info]))
	"""


def check_hidden_sub_row(self):
	row_missing_vals = {}
	row = 4

	for i in range(9):  # col goes across
		this_cell = (row, i)

		# stuff here



