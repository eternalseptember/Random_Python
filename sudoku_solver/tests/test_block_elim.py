"""
BLOCK ELIM ROWS:
In the central row of boxes:
8 can't be in (rows 3 to 5; cols 2 to 3).
8 can only be in (rows 3 and 5; cols 0 to 1) and (rows 3 and 5; cols 4 to 5).

So in the third box:
8 can only be in (row 4; cols 6 to 8).
Eliminate 8 from (rows 3 and 5; cols 6 to 8)
"""

import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("block_elim_row.txt")
sudoku.print_board()
print('===============================')



# Testing steps
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
# sudoku.print_possible_values()

"""
print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
sudoku.print_possible_values()
"""


print('Test block interaction')
sudoku.check_block_row((3, 0))
sudoku.print_possible_values()






