def answer(area):
	"""
	Input: total area of solar panels, [1 to 100,000]

	Output: return a list of the areas of the largest squares one
	could make out of those panels, starting with the largest
	squares first
	"""

	panels = []
	remaining = area

	while (remaining > 0):
		square = findLargestSquare(remaining)
		print(square)
		panels.append(square)
		remaining -= square

	return panels


def findLargestSquare(num):
	"""
	Find the largest square number that is less than num.
	"""
	factor = 1
	largestSquare = 1
	while (largestSquare < num):
		square = factor * factor
		if (square < num):
			largestSquare = square
		else:
			break
		factor += 1

	return largestSquare


print(answer(12))
print(answer(15324))
