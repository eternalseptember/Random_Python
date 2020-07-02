from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_1.txt")
print('Init board:')
sudoku.print_board()



# Testing steps
print('Reduce list of possibilities:')
sudoku.init_reduce()

print('Solve:')
sudoku.solve()
sudoku.print_board()
sudoku.print_possible_values()










