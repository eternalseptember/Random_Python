def calculate_hourglass_sum(arr, x, y):
	top_row = arr[x][y] + arr[x][y+1] + arr[x][y+2]
	mid_row = arr[x+1][y+1]
	bot_row = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
	return top_row + mid_row + bot_row




# arr[row_num][col_num]
# arr[0][0] = 1
# arr[0][1] = 1
# arr[1][0] = 0
arr = [[1, 1, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0],
		[1, 1, 1, 0, 0, 0],
		[0, 0, 2, 4, 4, 0],
		[0, 0, 0, 2, 0, 0],
		[0, 0, 1, 2, 4, 0]]


highest_sum = 0
for y in range(4):		# row[][y]
	for x in range(4):	# row[x][]
		this_sum = calculate_hourglass_sum(arr, x, y)
		if this_sum > highest_sum:
			highest_sum = this_sum


print(highest_sum)
