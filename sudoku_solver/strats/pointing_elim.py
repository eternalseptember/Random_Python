"""
Similar to poss_elim functions.

When a pair or triple is fully confined into a row or col within a box,
eliminate those values from the rest of the row or col, particularly when
there are other potential locations for the eliminated vals within their boxes.
"""


def pointing_elim(self):

	for i in [0, 3, 6]:  # i goes down.
		for j in [0, 3, 6]:  # j goes across.
			coord = (i, j)





