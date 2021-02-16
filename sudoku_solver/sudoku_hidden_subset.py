# Similar to naked subset.
# Import into the main sudoku_solver class.


def check_hidden_subsets(self):
	# Temporarily using this function to test.

	# self.check_hidden_sub_col()
	# self.check_hidden_sub_row()
	self.check_hidden_sub_box()


def check_hidden_sub_col(self):
	col_missing_vals = {}  # get list of missing values of this col
	col = 0  # manually setting for now

	for j in range(9):  # row goes down, col is constant
		this_cell = (j, col)
		self.set_missing_val_table(this_cell, col_missing_vals)


	for info in col_missing_vals.keys():
		print('{0}: {1}'.format(info, col_missing_vals[info]))



def check_hidden_sub_row(self):
	row_missing_vals = {}
	row = 4  # manually setting for now

	for i in range(9):  # col goes across
		this_cell = (row, i)

		# stuff here
		self.set_missing_val_table(this_cell, row_missing_vals)


	for info in row_missing_vals.keys():
		print('{0}: {1}'.format(info, row_missing_vals[info]))


def check_hidden_sub_box(self):
	# probably do a naked subset version of this function as well?
	# iterate boxes like in previous functions

	ref_box = (3, 3)  # manually setting to center box
	ref_row, ref_col = ref_box
	box_row = ref_row // 3
	box_col = ref_col // 3
	box_missing_vals = {}

	for i in range(3):
		for j in range(3):
			this_row = box_row * 3 + i
			this_col = box_col * 3 + j
			# print('({0}, {1})'.format(this_row, this_col))

			this_cell = (this_row, this_col)
			self.get_box_poss_vals(this_cell)


			# self.set_missing_val_table(this_cell, box_missing_vals)

	# print missing val dict
	# for item in box_missing_vals.keys():
	# 	print('{0}: {1}'.format(item, box_missing_vals[item])








