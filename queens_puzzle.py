from modules.test import *

def share_diagonal(x0, y0, x1, y1):
	""" Is (x0, y0) on a shared diagonal with (x1, y1)? """
	dy = abs(y1 - y0)	# Calc the absolute y distance
	dx = abs(x1 - x0)	# Calc the absolute x distance
	return dx == dy


test(not share_diagonal(5, 2, 2, 0))
test(share_diagonal(5, 2, 3, 0))
test(share_diagonal(5, 2, 4, 3))
test(share_diagonal(5, 2, 4, 1))