# Import into the main sudoku_solver class.
# Apparently, there's a difference between "naked triple" and "hidden triple".



def check_naked_triples(self):
	self.check_naked_triples_col()



def check_naked_triples_col(self):
	# collect every possibility first
	row = 4

	for i in range(9):
		this_cell = (row, i)

