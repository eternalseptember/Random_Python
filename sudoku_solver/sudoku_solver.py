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
		for row in self.board:
			print(row)


	def solve(self):
		# import the board first
		return None



