"""
Test file for puzzle_5.
Not yet solved.
"""

from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_5.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
sudoku.print_possible_values()


print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
sudoku.print_possible_values()









