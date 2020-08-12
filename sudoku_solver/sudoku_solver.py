# Input a formatted file with a sudoku puzzle.
# Print solved puzzle.


class Sudoku_Solver():
	from sudoku_print import print_board, print_possible_values, \
		print_init_queue, print_solved_queue

	from sudoku_unique import check_all_unique, check_unique_row, \
		check_unique_col, check_unique_box, set_lookup_table, \
		solve_lookup_table


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
		# If there isn't, then this location has been solved.
		if coord in self.possible_values:

			# Remove solved_value as a possible choice in this coord.
			poss_values = self.possible_values[coord]

			# Restructure this to remove a set of values?

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





	def check_matching_sets(self):
		# Run this if checking unique doesn't solve everything.
		"""
		elimination due to matching pairs will get both examples.
		are missing values all in the same box?

		tally each row/col's missing values.
		In puzzle_5:
		column 6 is missing 4 and 6, which are in the same box.
		Remove possibilities outside this col within this box (0-2, 7),
		because col is mostly solved, but box is not.


		tally each box's missing values.
		In puzzle_5:
		the missing values of the central box are in the same col, so remove
		6 and 9 as possiblities outside the box in the same column (row, 4).
		Remove possibilities from same col outside of this box,
		because box is mostly solved, but col is not.


		1. remove from row or col first.
		2. then if values share the same box, remove from the rest of the box.
		"""
		# self.check_matching_rows()
		self.check_matching_cols()



	def check_matching_rows(self):
		# search each row for pairs/triplets
		for row in range(9):
			row_missing_values = {}

			for i in range(9):  # i goes across
				this_cell = (row, i)






	def check_matching_cols(self):
		# search each col for pairs/triplets
		for col in range(9):
			col_missing_values = {}

			for j in range(9):  # j goes down
				this_cell = (j, col)

				if this_cell in self.possible_values:
					poss_values = self.possible_values[this_cell]

					# convert to hashable key
					poss_str = ''.join(map(str, poss_values))

					# add it in the missing_values dict?
					if poss_str in col_missing_values:
						col_missing_values[poss_str] += 1
					else:
						col_missing_values[poss_str] = 1


			# print the missing values
			print('\trow {0} missing: '.format(col))
			for missing_val in col_missing_values.keys():
				print('{0}: {1}'.format(missing_val, col_missing_values[missing_val]))


			print('turn missing_val back into lists')
			for missing_val in col_missing_values.keys():
				if len(missing_val) == col_missing_values[missing_val]:
					# remove these values from the rest of the col

					# turn missing_val back into a list
					missing_val_list = [int(val) for val in missing_val]
					print(missing_val_list)





	def remove_matching_sets(self, matching_sets, poss_vals):
		# matching_sets is a list of coordinates.
		# poss_vals is a list of integers.
		# length of both lists should match.
		print()
















