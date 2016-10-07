def answer(area):
	"""
	Input: total area of solar panels, [1 to 100,000]

	Output: return a list of the areas of the largest squares one
	could make out of those panels, starting with the largest
	squares first
	"""
	panels = []
	remaining = area
	listOfSquares = generateListOfSquares(area)

	while (remaining > 0):
		square = findLargestSquare(listOfSquares, remaining)
		# print(square)
		panels.append(square)
		remaining -= square

	return panels


def findLargestSquare(listOfSquares, num):
	if (len(listOfSquares) <= 1):
		return 1

	largestSquare = listOfSquares.pop()
	while largestSquare > num:
		largestSquare = listOfSquares.pop()

	return largestSquare


def generateListOfSquares(num):
	"""
	Generate the list of squares that is less than or equal to num.
	"""
	factor = 1
	largestSquare = 1
	listOfSquares = []

	while (largestSquare <= num):
		square = factor * factor
		if (square <= num):
			listOfSquares.append(square)
			largestSquare = square
			# print(square)
		else:
			break
		factor += 1

	return listOfSquares


# test = [12, 15324, 4]
test = [4]

for area in test:
	list = answer(area)
	print('Area: {0}'.format(area))
	print(list)
