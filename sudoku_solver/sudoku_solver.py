# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	from sudoku_print import print_board, print_possible_values, \
		print_init_queue, print_solved_queue


	def __init__(self):
		self.input = None
		self.board = self.create_board()
		self.possible_values = {}  # {(row, col): [possible values]}
		self.init_queue = []  # from init pass
		self.solved_list = []
		self.solved_queue = []


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
				cell_value = board_line[col]

				if cell_value == '-':
					self.possible_values[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
				else:
					cell_value = int(cell_value)
					self.board[row][col] = cell_value
					self.init_queue.append((row, col))


	def init_reduce(self):
		# Reduce list of possible values.
		# solved_value is the number on the board on first pass.
		while len(self.init_queue) > 0:
			solved_cell = self.init_queue.pop(0)
			self.solved_list.append(solved_cell)

			row, col = solved_cell
			solved_value = self.board[row][col]
			self.remove_num(solved_cell, solved_value)

		self.solve_queue()


	def solve_queue(self):
		# solved_value is a reduced list after the first pass.
		while len(self.solved_queue) > 0:
			solved_cell = self.solved_queue.pop()
			self.resolve(solved_cell)


	def resolve(self, coord):
		# Assign solved value to board and clean up lists.
		self.solved_list.append(coord)

		row, col = coord
		solved_value = self.possible_values.pop(coord)
		self.board[row][col] = solved_value[0]  # Set the value.
		self.remove_num(coord, solved_value[0])


	def remove_num(self, coord, solved_value):
		self.remove_num_in_row(coord, solved_value)
		self.remove_num_in_col(coord, solved_value)
		self.remove_num_in_box(coord, solved_value)


	def remove_num_in_row(self, coord, solved_value):
		# Remove solved_value from the possible list of values of
		# other unsolved cells in this row.
		ref_row, ref_col = coord  # Reference cell

		for i in range(9):
			if i != ref_col:
				this_cell = (ref_row, i)
				self.possible_vals_check(this_cell, solved_value)


	def remove_num_in_col(self, coord, solved_value):
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
			poss_values = self.possible_values[coord]

			if solved_value in poss_values:
				poss_values.remove(solved_value)

			# Add to queue if only one possible value is remaining.
			if len(poss_values) == 1:
				if (coord not in self.init_queue) and \
					(coord not in self.solved_list) and \
					(coord not in self.solved_queue):
					self.solved_queue.append(coord)


	def solve(self, coord):
		# To manually resolve one individual cell.
		self.resolve(coord)
		self.solve_queue()


	def check_all_unique(self):
		# check all row
		for row in range(9):
			self.check_unique_row((row, 0))

		# check all col
		for col in range(9):
			self.check_unique_col((0, col))

		# check all box
		for i in [0, 3, 6]:
			for j in [0, 3, 6]:
				coord = (i, j)
				self.check_unique_box(coord)


	def check_unique_row(self, coord):
		ref_row, ref_col = coord  # Reference cell
		val_lookup = {}  # {value: [(possible cells)]}

		# List all possible locations of all missing values.
		for i in range(9):
			this_cell = (ref_row, i)
			self.set_lookup_table(this_cell, val_lookup)

		self.solve_lookup_table(val_lookup)


	def check_unique_col(self, coord):
		ref_row, ref_col = coord  # Reference cell
		val_lookup = {}  # {value: [(possible cells)]}

		# List all possible locations of all missing values.
		for j in range(9):
			this_cell = (j, ref_col)
			self.set_lookup_table(this_cell, val_lookup)

		self.solve_lookup_table(val_lookup)


	def check_unique_box(self, coord):
		# Look within a 3x3 box and check for unique listing.
		ref_row, ref_col = coord  # Reference cell
		val_lookup = {}  # {value: [(possible cells)]}

		# Possible values: 0, 1, 2
		box_row = ref_row // 3
		box_col = ref_col // 3

		# List all possible locations of all missing values.
		for i in range(3):
			for j in range(3):
				row = box_row * 3 + i
				col = box_col * 3 + j
				this_cell = (row, col)

				self.set_lookup_table(this_cell, val_lookup)

		self.solve_lookup_table(val_lookup)


	def set_lookup_table(self, coord, lookup_dict):
		# List possible coordinates for each value.
		if coord in self.possible_values:
			poss_values = self.possible_values[coord]

			for poss_value in poss_values:
				if poss_value not in lookup_dict:
					lookup_dict[poss_value] = [coord]
				else:
					lookup_dict[poss_value].append(coord)


	def solve_lookup_table(self, lookup_dict):
		# Does any missing value have only one possible location?
		for poss_value in lookup_dict.keys():
			poss_locs = len(lookup_dict[poss_value])
			if poss_locs == 1:
				new_coord = lookup_dict[poss_value][0]
				print('{0} is in {1}'.format(poss_value, new_coord))

				self.possible_values[new_coord] = [poss_value]
				self.solve(new_coord)














