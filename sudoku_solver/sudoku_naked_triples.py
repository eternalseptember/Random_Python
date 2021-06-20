# Import into the main sudoku_solver class.
"""
Naked triple: 
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""


def check_naked_triples(self):
	self.check_naked_triples_col()



def check_naked_triples_col(self):
	# collect every possibility first
	row = 4
	col_missing_vals = {}

	for i in range(9):
		this_cell = (row, i)
		self.set_lookup_table(this_cell, col_missing_vals)


	# possible_subsets = self.find_naked_triple(col_missing_vals)
	# print(possible_subsets)
	# self.clean_hidden_subsets()


	for key in col_missing_vals.keys():
		print('{0}: {1}'.format(key, col_missing_vals[key]))




def find_naked_triple(self, missing_vals):
	# How to identify group?
	naked_subsets = {}


	return naked_subsets





