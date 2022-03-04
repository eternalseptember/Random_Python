"""
7 is locked to rows [1, 5] and cols [3, 7].
7 as a possible value is removed from:
(0, 3)
(4, 3)
(7, 3) and (7, 7)
(8, 3) and (8, 7)

"""


import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("xwing_1.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check xwing:')
sudoku.check_xwing()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')






