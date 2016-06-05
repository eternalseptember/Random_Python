import turtle

def draw_multicolor_square(t, sz):
	""" Make turtle t draw a multi-color square of sz. """
	for i in ["red", "purple", "hotpink", "blue"]:
		t.color(i)
		t.forward(sz)
		t.left(90)


wn = turtle.Screen() 		# creates a playground for turtles
wn.bgcolor("lightgreen")

'''
# turtles in a spiral
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size=20
for i in range(30):
	tess.stamp()	# leave an impression on the canvas
	size += 3		# increase the size on every iteration
	tess.forward(size)
	tess.right(24)

tess.color("yellow")
'''

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(15):
	draw_multicolor_square(tess,size)
	size += 10
	tess.forward(10)
	tess.right(18)

wn.mainloop()