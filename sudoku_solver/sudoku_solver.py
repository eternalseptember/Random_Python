# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	def __init__(self):
		self.input = None
		self.board = self.create_board()
		self.possible_values = {}  # {{row, col}: [possible values]}


	def create_board(self):
		board = [
			['-' for col in range(9)] for row in range(9)
			]
		return board


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


	def print_possible_values(self):
		for coord in self.possible_values.keys():
			possibilities = self.possible_values[coord]
			print('{0}: {1}'.format(coord, possibilities))


	def import_board(self, file_name):
		board_file = open(file_name, 'r')
		board_import = board_file.readlines()
		board_file.close()

		for row in range(9):
			board_line = board_import[row].rstrip()
			for col in range(9):
				loc_value = board_line[col]

				if loc_value == '-':
					continue
				else:
					loc_value = int(loc_value)
					self.board[row][col] = loc_value


	def solve(self):
		# look for obvious results first
		return None


	def check_box(self, row, col):
		# remove them from the list if they're present in the box
		possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		empty_cells = []  # (row, col)

		# possible values: 0, 1, 2
		box_row = row // 3
		box_col = col // 3

		# iterate through an entire 3x3 box
		for i in range(3):
			row_index = box_row * 3 + i

			for j in range(3):
				col_index = box_col * 3 + j

				grid_item = self.board[row_index][col_index]

				if grid_item == '-':
					empty_cells.append((row_index, col_index))
				else:
					possible_values.remove(grid_item)

		# just testing to see if it works




	def check_row(self, row, col):
		return None


	def check_col(self, row, col):
		return None












