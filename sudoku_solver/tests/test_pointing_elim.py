# testing whether current functions can eliminate possible values based on
# pointing pairs or triples


import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/test_pointing_elim.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')

"""
print('Single-box block-level eliminations:')
sudoku.check_within_boxes()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Double-boxed block-level eliminations:')
sudoku.check_block_elim()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')
"""










