from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_2.txt")
sudoku.print_board()
print('===============================')



# Testing steps
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
sudoku.print_possible_values()

print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()












