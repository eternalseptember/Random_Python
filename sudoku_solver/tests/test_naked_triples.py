"""
Naked triple: 
Not all cells must contain all three candidates, but there must not be more
than three candidates in the three cells all together.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("naked_triple_row.txt")
sudoku.print_board()
print('===============================')


# Testing steps
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')




print('Check for naked triples:')
sudoku.check_naked_triples()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')








