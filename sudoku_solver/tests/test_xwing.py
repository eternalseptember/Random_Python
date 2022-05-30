"""
	xwing_test_1:
4 is locked to rows [2, 4] and cols [1, 4].
4 as a possible value is removed from:
    (0, 1) and (0, 4)
    (1, 1) and (1, 4)
    (5, 1) and (5, 4)


	xwing_test_2:
8 is locked to rows [1, 3] and cols [4, 6].
8 as a possible value is removed from:
	(2, 6) and (4, 4)
"""


import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
# sudoku.import_board("test_boards/xwing_test_1.txt")
sudoku.import_board("test_boards/xwing_test_2.txt")
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


print('Check xwing again:')
sudoku.check_xwing()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')









