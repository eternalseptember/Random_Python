from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_1.txt")
sudoku.print_board()
print('===============================')



# Testing steps
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
sudoku.print_possible_values()

print('Unique lookup test:')
# sudoku.check_unique_box((0, 0))
# sudoku.check_unique_row((3, 0))  # doesn't solve everything
# sudoku.check_unique_row((6, 0))

# doesn't solve everything
for col in range(9):
	sudoku.check_unique_col((0, col))

sudoku.print_board()












