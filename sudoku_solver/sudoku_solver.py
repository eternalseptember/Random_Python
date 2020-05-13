# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	def __init__(self):
		self.input = None
		self.board = self.create_board()


	def create_board(self):
		board = [
			['-' for col in range(9)] for row in range(9)
			]
		return board


	def import_board(self, file_name):
		board_file = open(file_name, 'r')
		board_import = board_file.readlines()
		board_file.close()

		for row in range(9):
			board_line = board_import[row].rstrip()
			for col in range(9):
				loc_value = board_line[col]
				print(loc_value, end='')

				if loc_value == '-':
					continue
				else:
					loc_value = int(loc_value)
					self.board[row][col] = loc_value
			print()



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


	def check_row(self, row, col):
		return None


	def check_col(self, row, col):
		return None


	def check_box(self, row, col):
		return None










