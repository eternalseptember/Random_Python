"""
Test file for puzzle_6.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/puzzle_6.txt")
sudoku.print_board()
print('===============================')









