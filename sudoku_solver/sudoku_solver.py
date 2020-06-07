# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	def __init__(self):
		self.input = None
		self.board = self.create_board()
		self.possible_values = {}  # {{row, col}: [possible values]}
		self.solved_queue = []  # to trigger removing values


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
		# Look for obvious results first.
		return None


	def check_box(self, coord):
		row, col = coord

		# Remove them from the list if they're present in the box
		possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		empty_cells = []  # (row, col)

		# Possible values: 0, 1, 2
		box_row = row // 3
		box_col = col // 3

		# Iterate through an entire 3x3 box.
		for i in range(3):
			row_index = box_row * 3 + i

			for j in range(3):
				col_index = box_col * 3 + j

				grid_item = self.board[row_index][col_index]

				if grid_item == '-':
					empty_cells.append((row_index, col_index))
				else:
					possible_values.remove(grid_item)

		# split function here.
		# previous section is for populating possible vals.
		# just testing to see if it works
		print('\nMissing numbers in this box:')
		print(possible_values)
		print()

		for cell in empty_cells:
			cell_poss_vals = possible_values.copy()

			# Eliminate values from checking row and col.
			self.check_row(cell, cell_poss_vals)
			self.check_col(cell, cell_poss_vals)

			# Write to dictionary of possible values.
			self.possible_values[cell] = cell_poss_vals



	def check_row(self, coord, list_of_poss_vals):
		# Reduce list of possible vals by other nums in row.
		row, col = coord

		for i in range(9):
			if i != row:
				grid_item = self.board[row][i]

				if grid_item != '-':
					if grid_item in list_of_poss_vals:
						list_of_poss_vals.remove(grid_item)

		# check if only one possible value left?



	def check_col(self, coord, list_of_poss_vals):
		# Reduce list of possible vals by other nums in col.
		row, col = coord

		for i in range(9):
			if i != col:
				grid_item = self.board[i][col]

				if grid_item != '-':
					if grid_item in list_of_poss_vals:
						list_of_poss_vals.remove(grid_item)

		# check if only one possible value left?




	def is_value(self, coord):
		# Check when a cell is solved.
		poss_values = self.possible_values[coord]

		if len(poss_values) == 1:
			return True
		else:
			return False



	def remove_value(self, coord):
		# When a value is set, remove that as a possibility in affected
		# bow, row, or col.
		row, col = coord
		
		return None


	def remove_num_in_row(self, coord, value):
		# opposite of the check_row function.
		row, col = coord

		for i in range(9):
			if i != row:
				grid_item = self.board[row][i]

				# check if it's an entry in possible_values
				if (row, i) in self.possible_values:
					possible_values = self.possible_values[(row, i)]

					if grid_item in possible_values:
						possible_values.remove(grid_item)


	def remove_num_in_col(self, coord, value):
		row, col = coord
		return None


	def test(self, coord, value):
		# for testing only
		# manually setting a value and testing the remove_num functions
		row, col == coord
		self.board[row][col] = value













