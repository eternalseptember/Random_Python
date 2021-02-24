# Similar to naked subset.
# Import into the main sudoku_solver class.


def check_hidden_subsets(self):
	# Temporarily using this function to test.

	self.check_hidden_sub_col()
	# self.check_hidden_sub_row()
	# self.check_hidden_sub_box()


def check_hidden_sub_col(self):
	col_missing_vals = {}  # get list of missing values of this col
	col = 8  # manually setting for now

	for j in range(9):  # row goes down, col is constant
		this_cell = (j, col)
		self.set_lookup_table(this_cell, col_missing_vals)


	# format info for subset analysis
	possible_subsets = {}
	for info in col_missing_vals.keys():
		subset_locs = col_missing_vals[info]
		print('{0}: {1}'.format(info, subset_locs))

		# need a separate function that does this better
		subset_str = ''.join(map(str, subset_locs))


		print('{0}'.format(subset_str))




def check_hidden_sub_row(self):
	row_missing_vals = {}
	row = 4  # manually setting for now

	for i in range(9):  # col goes across
		this_cell = (row, i)
		# stuff here




def check_hidden_sub_box(self):
	# probably do a naked subset version of this function as well?

	# The function that calls this will iterate the whole grid.
	# But for testing here, define a single box instead.
	ref_box = (3, 3)
	poss_values = self.get_box_poss_vals(ref_box)
	for item in poss_values.keys():
		print('{0}: {1}'.format(item, poss_values[item]))


	# Getting list of possible values in each location.
	print()
	for i in [3, 4, 5]:
		for j in [3, 4, 5]:
			this_cell = (i, j)
			if this_cell in self.possible_values:
				poss_values = self.possible_values[this_cell]
				print('{0}: {1}'.format(this_cell, poss_values))


	# ??? how to determine subset???
	# search through poss_values
	# if length of poss_values[item] is 2 or 3
	# add the missing value in a list... poss_pair or poss_trip?


	# Collect info about subset from previous step.
	# Subset check: X candidates can only be found in X cells...
	subset_vals = []
	subset_locs = []

	# [1, 8] could be in [(4, 3), (4, 5)]
	# go to [(4, 3), (4, 5)] and remove all other possibilities not in subset













