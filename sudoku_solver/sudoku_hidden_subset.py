# Similar to naked subset.
# Import into the main sudoku_solver class.


def analyze_hidden_subsets(self):
	return None


def analyze_hidden_sub_col(self):
	# get list of missing values of this col
	col_missing_vals = {}

	# manually setting for now
	col = 0

	for j in range(9):  # row goes down, col is constant
		this_cell = (j, col)
		self.set_missing_val_table(this_cell, col_missing_vals)





