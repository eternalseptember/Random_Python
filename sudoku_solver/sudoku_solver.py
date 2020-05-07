# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	def __init__(self):
		self.input = None
		self.board = self.create_board()


	def create_board(self):
		board = [
			[0 for col in range(9)] for row in range(9)
			]
		return board


	def import_board(self, file):
		return None


	def print_board(self):
		for row in range(9):
			if (row > 0) and (row % 3 == 0):
				print('-----------------')

			for col in range(9):
				if (col == 0):
					print(' ', end='')
				elif (col % 3 == 0):
					print(' | ', end='')

				print(self.board[row][col], end='')

			print()


	def solve(self):
		# import the board first
		return None



