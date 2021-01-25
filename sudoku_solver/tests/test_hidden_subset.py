"""
HIDDEN SUBSET COL:
There are three possible locations for 5,
but two of them are the only possible choices for 6 and 7.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("hidden_subset_col.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')









