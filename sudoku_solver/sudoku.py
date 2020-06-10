from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_1.txt")
sudoku.print_board()

"""
# initial fill
sudoku.check_box((0, 0))
sudoku.print_possible_values()

# manually inputting value
sudoku.test((5, 6), 8)
print('\nafter inputting test value')
sudoku.print_board()
"""


# try to get initial list of possible values first
row = 0
col = 0

for y in range(3):
	for x in range(3):
		sudoku.check_box((row, col))
		row += 3

	row = 0
	col += 3

sudoku.print_possible_values()



