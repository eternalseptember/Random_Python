import turtle

turtle.setup(400,400)
wn = turtle.Screen()
wn.title("Handling keypreses!")
wn.bgcolor("lightgreen")
squirtle = turtle.Turtle()

def h1():
	squirtle.forward(30)

def h2():
	squirtle.left(45)

def h3():
	squirtle.right(45)

def h4():
	wn.bye() #closes the turtle window

# These lines "wire up" keypresses to the handlers that were defined
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

# Tell the window to start listening for events.
# If any of the keys that is monitored is pressed,
# its handler will be called.
wn.listen()
wn.mainloop()