"""
Test file for puzzle_5.
Not yet solved.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_5.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Eliminate block-level possibilities:')
sudoku.check_within_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check unique locations:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')




