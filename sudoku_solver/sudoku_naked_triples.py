# Import into the main sudoku_solver class.
"""
Naked triple: 
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""


def check_naked_triples(self):
	self.check_naked_triples_row()



def check_naked_triples_row(self):
	# collect every possibility first
	row = 4
	row_missing_vals = {}
	poss_trips = []  # contains a list of dicts

	# get the possibilities in each cell, then compare?
	for i in range(9):
		this_cell = (row, i)
		poss_vals = self.possible_values[this_cell]

		# if the group is greater than three, then can't be part of the triple
		if len(poss_vals) > 3:
			continue
		else:
			# convert cells to string as key??
			trip_group = {}  # store the coordinates and possibilities\
			subset_str = ''

			# 

			poss_trips[this_cell] = poss_vals




	"""
	for i in range(9):
		this_cell = (row, i)
		self.set_lookup_table(this_cell, row_missing_vals)

	# this portion will become find_naked_triple()
	# for missing_val in row_missing_vals.keys():
	# 	print('{0}: {1}'.format(missing_val, row_missing_vals[missing_val]))

	possible_subsets = self.find_naked_triple(col_missing_vals)
	self.clean_hidden_subsets()

	"""


















def find_naked_triple(self, missing_vals):
	# How to identify group?
	naked_subsets = {}


	return naked_subsets





