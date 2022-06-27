# testing whether current functions can eliminate possible values based on
# pointing pairs or triples


import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("test_boards/test_elim.txt")
sudoku.print_board()
print('===============================')






