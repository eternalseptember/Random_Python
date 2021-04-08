"""
HIDDEN SUBSET COL 1:
[1,9] can only be in (4,8) and (6,8).
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
# sudoku.import_board("hidden_subset_box_1.txt")
sudoku.import_board("hidden_subset_col_1.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')



print('Find hidden subset:')
sudoku.check_hidden_subsets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


"""
print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')
"""







