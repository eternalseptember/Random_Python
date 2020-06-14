from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_1.txt")
sudoku.print_board()

"""
# initial fill
sudoku.init_check_box((0, 0))
sudoku.print_possible_values()

# manually inputting value
sudoku.test((5, 6), 8)
print('\nafter inputting test value')
sudoku.print_board()
"""


sudoku.solve()
# sudoku.print_possible_values()
sudoku.print_solved_queue()





