# Similar to naked subset.
# Import into the main sudoku_solver class.


def check_hidden_subsets(self):
	# Temporarily using this function to test.

	self.check_hidden_sub_col()
	# self.check_hidden_sub_row()
	# self.check_hidden_sub_box()


def check_hidden_sub_col(self):
	col = 8  # MANUALLY SETTING FOR TESTING
	col_missing_vals = {}  # get list of missing values of this col

	# Get list of possible values for each location.
	for j in range(9):  # row goes down, col is constant
		this_cell = (j, col)
		self.set_lookup_table(this_cell, col_missing_vals)

	# Check for subsets and then clean col.
	possible_subsets = self.check_hidden_subset_info(col_missing_vals)
	self.clean_hidden_subsets(possible_subsets, 'col')



def check_hidden_sub_row(self):
	row = 0  # MANUALLY SETTING FOR TESTING
	row_missing_vals = {}  # get list of missing values of this row

	# Get list of possible values for each location.
	for i in range(9):  # col goes across
		this_cell = (row, i)
		self.set_lookup_table(this_cell, row_missing_vals)

	# Check for subsets and then clean row.
	possible_subsets = self.check_hidden_subset_info(row_missing_vals)
	self.clean_hidden_subsets(possible_subsets, 'row')



def check_hidden_subset_info(self, missing_val_info):
	# missing_val_info is a dict with possible values in each location.
	# Format list of possibilties for subset analysis.
	possible_subsets = {}
	for missing_num in missing_val_info.keys():
		subset_locs = missing_val_info[missing_num]

		# Formats location of subset into a string.
		subset_str = ''
		for loc in subset_locs:
			if len(subset_str) > 0:
				subset_str += '-'
			loc_row, loc_col = (loc)
			subset_str += '{0},{1}'.format(loc_row, loc_col)


		if subset_str not in possible_subsets:
			possible_subsets[subset_str] = {
				'subset_locs': subset_locs,
				'missing_num': [missing_num]
			}
		else:
			subset_info = possible_subsets[subset_str]
			subset_info['missing_num'].append(missing_num)

	return possible_subsets



def clean_hidden_subsets(self, possible_subsets, label=''):
	# mode is 'col' or 'row'
	for item_key in possible_subsets.keys():
		item = possible_subsets[item_key]
		subset_locs = item['subset_locs']
		missing_nums = item['missing_num']

		# a function that captures this needs to adjust for col or row
		if len(missing_nums) == len(subset_locs):
			if label == 'col':
				self.remove_hidden_col(item)
			elif label == 'row':
				self.remove_hidden_row(item)



def remove_hidden_col(self, subset_info):
	# Goes down a col and cleans up subset possibilities.
	# subset_info is dict with keys 'subset_locs' and 'missing_num'
	subset_locs = subset_info['subset_locs']
	subset_nums = subset_info['missing_num']

	# Get the column number.
	first_coord = subset_locs[0]
	coord_row, coord_col = first_coord

	# Clean up the column based on knowledge of subset.
	for i in range(9):  # row goes down, col is constant
		coord = (i, coord_col)

		# Unsolved cell. Could be part of the subset or not.
		if coord in self.possible_values:
			poss_values = self.possible_values[coord]

			# If coord IS part of the subset, subset_locs,
			# then remove poss_values that are not in subset_nums.
			if coord in subset_locs:
				new_poss_vals = \
					[poss_val for poss_val in poss_values if poss_val in subset_nums]

			else:
				# coord is NOT part of the subset,
				# so remove subset_nums from poss_values.
				new_poss_vals = \
					[poss_val for poss_val in poss_values if poss_val not in subset_nums]

			self.possible_values[coord] = new_poss_vals


			# Then check if solved.
			if len(poss_values) == 1:
				if (coord not in self.solved_list) and \
					(coord not in self.solved_queue):
					self.solved_queue.append(coord)




def remove_hidden_row(self, subset_info):
	# Goes across a row and cleans up subset possibilities.
	# subset_info is dict with keys 'subset_locs' and 'missing_num'
	subset_locs = subset_info['subset_locs']
	subset_nums = subset_info['missing_num']


	# Get the row number.
	# COULD BE PASSED FROM THE FUNCTION CALLING THIS.
	first_coord = subset_locs[0]
	coord_row, coord_col = first_coord

	# Clean up the row based on knowledge of subset.
	for j in range(9):  # col goes down, row is constant
		coord = (coord_row, j)

		# Unsolved cell. Could be part of the subset or not.
		if coord in self.possible_values:
			poss_values = self.possible_values[coord]



def clean_hidden_subset(self, coord, subset_locs, subset_nums):
	# Unsolved cell. Could be part of the subset or not.
	if coord in self.possible_values:
		poss_values = self.possible_values[coord]

		if coord in subset_locs:
			new_poss_vals = \
				[poss_val for poss_val in poss_values if poss_val in subset_nums]
		else:
			# coord is NOT part of the subset,
			# so remove subset_nums from poss_values.
			new_poss_vals = \
				[poss_val for poss_val in poss_values if poss_val not in subset_nums]

		# new_poss_vals comes from the if/else statement.
		self.possible_values[coord] = new_poss_vals












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













