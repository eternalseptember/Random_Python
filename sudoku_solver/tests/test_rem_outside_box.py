from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
# sudoku.import_board("check_within_box_row_test.txt")
sudoku.import_board("check_within_box_col_test.txt")
sudoku.print_board()
print('===============================')



# Testing steps
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
# sudoku.print_possible_values()


print('Check within box:')
sudoku.check_within_a_box((4, 4))
sudoku.print_board()
sudoku.print_possible_values()






