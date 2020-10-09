from sudoku_solver import *


# Test stuff
sudoku = Sudoku_Solver()
sudoku.import_board("sudoku_test_5.txt")
sudoku.print_board()
print('===============================')



# Testing steps
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
# sudoku.print_possible_values()


"""
print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()
"""

"""
print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
sudoku.print_possible_values()
"""






