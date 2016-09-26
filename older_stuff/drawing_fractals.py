# Studying recursion
import turtle


def koch(t, order, size):
	"""
	Make turtle t draw a Koch fractal of 'order' and 'size'.
	Leave the turtle facing the same direction.
	"""
	if order == 0:	# The base case is just a straight line
		t.forward(size)
	else:
		'''
		for angle in [60, -120, 60, 0]:
			koch(t, order-1, size/3)
			t.left(angle)
		'''
		koch(t, order-1, size/3)   # Go 1/3 of the way
		t.left(60)
		koch(t, order-1, size/3)
		t.right(120)
		koch(t, order-1, size/3)
		t.left(60)
		koch(t, order-1, size/3)



turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Drawing fractals")
wn.bgcolor("lightgreen")
squirtle = turtle.Turtle()
squirtle.color("blue")

# set start position
squirtle.penup()
squirtle.goto(-300, 0)
squirtle.pendown()


koch(squirtle, 4, 400)



wn.mainloop()