"""
HIDDEN SUBSET COL 1:
[1,9] can only be in (4,8) and (6,8).

HIDDEN SUBSET ROW 1:
[4,7] can only be in (0,0) and (0,1).

HIDDEN SUBSET BOX 1:
[1,8] can only be in (4,3) and (4,5).
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
# sudoku.import_board("hidden_sub_box_1.txt")
# sudoku.import_board("hidden_sub_col_1.txt")
sudoku.import_board("hidden_sub_row_1.txt")
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






