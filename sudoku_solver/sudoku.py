from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_1.txt")
sudoku.print_board()
sudoku.check_box((0, 0))
sudoku.print_possible_values()


