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

	self.find_naked_triple(col_missing_vals)



def find_naked_triple(self, missing_vals):
	return None





