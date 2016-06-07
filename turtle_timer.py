import turtle

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

squirtle = turtle.Turtle()
squirtle.color("purple")
squirtle.pensize(3)

def h1():
	squirtle.forward(100)
	squirtle.left(56)
	wn.ontimer(h1, 60)

h1()
wn.mainloop()