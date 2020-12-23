"""
BLOCK ELIM ROWS:
In the central row of boxes:
8 can't be in (rows 3 to 5; cols 2 to 3).
8 can only be in (rows 3 and 5; cols 0 to 1) and (rows 3 and 5; cols 4 to 5).

So in the third box:
8 can only be in (row 4; cols 6 to 8).
Eliminate 8 from (rows 3 and 5; cols 6 to 8)


BLOCK ELIM COLS:
In the top two rows:
8 can't be in (rows 2 and 3).

In the middle box of the last row:
8 can only be in (rows 6 to 8; col 4).
Eliminate 8 from (rows 6 to 8; cols 3 and 5).
"""

import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("block_elim_row.txt")
# sudoku.import_board("block_elim_col.txt")
sudoku.print_board()
print('===============================')



# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')

"""
print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
"""


print('Test block interaction:')
# sudoku.check_within_boxes()
sudoku.check_block_elim()
# sudoku.print_board()
sudoku.print_possible_values()
print('===============================')





