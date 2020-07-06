from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_1.txt")
sudoku.print_board()
print('===============================')



# Testing steps
sudoku.init_reduce()
# sudoku.solve()
sudoku.print_board()
sudoku.print_possible_values()

print('Unique lookup test:')
sudoku.check_unique_box((0, 0))
sudoku.print_board()
sudoku.print_possible_values()











