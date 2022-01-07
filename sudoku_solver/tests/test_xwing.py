
# 7 is locked to rows [1, 5] and cols [3, 7].



import sys
sys.path.append('../')
from sudoku_solver import *


# Test puzzles of various difficulty levels.
sudoku = Sudoku_Solver()
sudoku.import_board("xwing_1.txt")
sudoku.print_board()
print('===============================')





