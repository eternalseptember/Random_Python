import turtle

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Handling mouse clicks!")
wn.bgcolor("lightgreen")

squirtle = turtle.Turtle()
squirtle.color("purple")
squirtle.pensize(3)
squirtle.shape("circle")

wartortle = turtle.Turtle()
wartortle.color("blue")

def handler_for_squirtle(x, y):
	wn.title("Squirtle clicked at {0}, {1}".format(x, y))
	#squirtle.goto(x, y)
	squirtle.left(42)
	squirtle.forward(30)

def handler_for_wartortle(x, y):
	wn.title("Wartortle clicked at {0}, {1}".format(x, y))
	wartortle.right(84)
	wartortle.forward(50)

# wn.onclick(h1) # wire up a click on the window
squirtle.onclick(handler_for_squirtle)
wartortle.onclick(handler_for_wartortle)

wn.mainloop()