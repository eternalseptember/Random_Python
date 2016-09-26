import turtle

def make_window(color, title):
	""" Set up the window with the given background color and title.
	Returns the new window. """
	w = turtle.Screen()
	w.bgcolor(color)
	w.title(title)
	return w

def make_turtle(color, size):
	""" Set up a turtle with the given color and pen size.
	Returns the new turtle. """
	t = turtle.Turtle()
	t.color(color)
	t.pensize(size)
	return t

def draw_bar(t, height):
	""" Get turtle t to draw one bar of height. """
	t.begin_fill()
	t.left(90)
	t.forward(height)		# draw up the left side
	t.write("  " + str(height)) # prints the height above the bar
	t.right(90)
	t.forward(40)			# width of bar, along the top
	t.right(90)
	t.forward(height)		# and down again!
	t.left(90)				# put the turtle facing the way we found it
	t.end_fill()
	t.forward (10)			# leave small gap after each bar


wn = make_window("lightgreen", "draw bar chart")
squirtle = make_turtle("blue", 3)
squirtle.color("blue", "red")

xs = [48, 117, 200, 240, 160, 260, 220]
for v in xs:
	draw_bar(squirtle,v)


wn.mainloop()