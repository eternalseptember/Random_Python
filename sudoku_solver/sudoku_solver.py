# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	from sudoku_print import print_board, print_possible_values, \
		print_solved_queue


	def __init__(self):
		self.input = None
		self.board = self.create_board()
		self.possible_values = {}  # {(row, col): [possible values]}
		self.solved_queue = []  # to trigger removing values


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

				if loc_value == '-':
					continue
				else:
					loc_value = int(loc_value)
					self.board[row][col] = loc_value


	def solve(self):
		# Look for obvious results first.
		# Initial list of possible values.
		row = 0
		col = 0

		for y in range(3):
			for x in range(3):
				self.init_check_box((row, col))
				row += 3

			row = 0
			col += 3

		# Check solved queue.



	def init_check_box(self, coord):
		row, col = coord

		# Remove them from the list if they're present in the box
		possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		empty_cells = []  # (row, col)

		# Possible values: 0, 1, 2
		box_row = row // 3
		box_col = col // 3

		# Iterate through an entire 3x3 box,
		# make a list of empty cells, and
		# remove existing board nums in this box from list of possible values.
		for i in range(3):
			for j in range(3):
				row_index = box_row * 3 + i
				col_index = box_col * 3 + j

				board_val = self.board[row_index][col_index]

				if board_val == '-':
					empty_cells.append((row_index, col_index))
				else:
					possible_values.remove(board_val)


		# Split function here.
		# previous section is for populating possible vals.

		for cell in empty_cells:
			cell_poss_vals = possible_values.copy()

			# Eliminate values from checking row and col.
			self.init_check_row(cell, cell_poss_vals)
			self.init_check_col(cell, cell_poss_vals)

			# Write to dictionary of possible values.
			self.possible_values[cell] = cell_poss_vals

			# Check if only one value remaining?
			# Add to queue.
			if len(cell_poss_vals) == 1:
				if cell not in self.solved_queue:
					self.solved_queue.append(cell)



	def init_check_row(self, coord, list_of_poss_vals):
		# Reduce list of possible vals by other existing board nums in row.
		ref_row, ref_col = coord  # Reference cell

		for i in range(9):
			if i != ref_row:
				board_val = self.board[ref_row][i]

				if board_val != '-':
					if board_val in list_of_poss_vals:
						list_of_poss_vals.remove(board_val)

		# check if only one possible value left?


	def init_check_col(self, coord, list_of_poss_vals):
		# Reduce list of possible vals by other existing board nums in col.
		ref_row, ref_col = coord  # Reference cell

		for j in range(9):
			if j != ref_col:
				board_val = self.board[j][ref_col]

				if board_val != '-':
					if board_val in list_of_poss_vals:
						list_of_poss_vals.remove(board_val)

		# check if only one possible value left?


	def solved(self, coord):
		# Set the value.
		# When a value is set, remove that as a possibility in affected
		# bow, row, or col.
		print('Solving {0}'.format(coord))
		row, col = coord

		solved_value = self.possible_values[coord]

		self.board[row][col] = solved_value[0]

		# Remove from possible_values?
		self.remove_num_in_row(coord, solved_value[0])
		self.remove_num_in_col(coord, solved_value[0])
		# self.remove_num_in_box(coord, solved_value[0])

		# Clean up solved_queue?
		# Maybe not because it'll disrupt the while loop running this?



	def remove_num_in_row(self, coord, solved_value):
		# Opposite of the init_check_row function.
		# Remove solved_value from the possible list of values of
		# other unsolved cells in this row.
		ref_row, ref_col = coord  # Reference cell

		for i in range(9):
			if i != ref_col:
				this_cell = (ref_row, i)
				self.possible_vals_check(this_cell, solved_value)


	def remove_num_in_col(self, coord, solved_value):
		# Opposite of the init_check_col function.
		# Remove solved_value from the possible list of values of
		# other unsolved cells in this col.
		ref_row, ref_col = coord  # Reference cell

		for j in range(9):
			if j != ref_row:
				this_cell = (j, ref_col)
				self.possible_vals_check(this_cell, solved_value)


	def remove_num_in_box(self, coord, solved_value):
		# Remove solved_value from the possible list of values of
		# other unsolved cells in this box.
		ref_row, ref_col = coord  # Reference cell

		# Possible values: 0, 1, 2
		box_row = ref_row // 3
		box_col = ref_col // 3

		# Iterate through one box.
		for i in range(3):
			for j in range(3):
				row = box_row * 3 + i
				col = box_col * 3 + j
				this_cell = (row, col)
				self.possible_vals_check(this_cell, solved_value)


	def possible_vals_check(self, coord, solved_value):
		# Check if there is a stored list of possible values in this coord.
		if coord in self.possible_values:

			# Remove solved_value as a possible choice in this coord.
			possible_values = self.possible_values[coord]

			if solved_value in possible_values:
				possible_values.remove(solved_value)

			# Add to queue if only one possible value is remaining.
			if len(possible_values) == 1:
				# Check if cell is already solved?
				if coord not in self.solved_queue:
					self.solved_queue.append(coord)













