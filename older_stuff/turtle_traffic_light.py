# programming a state machine in python
import turtle

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Squirtle does a traffic light!")
wn.bgcolor("white")
squirtle = turtle.Turtle()

def draw_housing():
	""" Draw a housing to hold the traffic lights. """
	squirtle.pensize(3)
	squirtle.color("black", "darkgrey")
	squirtle.begin_fill()
	squirtle.forward(80)
	squirtle.left(90)
	squirtle.forward(200)
	squirtle.circle(40, 180)
	squirtle.forward(200)
	squirtle.left(90)
	squirtle.end_fill()


draw_housing()

squirtle.penup()
# Position squirtle into the place where the green light should be
squirtle.forward(40)
squirtle.left(90)
squirtle.forward(50)
# Turn squirtle into a big green circle
squirtle.shape("circle")
squirtle.shapesize(3)
squirtle.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Yellow, Red. We number these states 0, 1, 2.
# When the machine changes state, we change squirtle's position
# and its fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
	global state_num
	if state_num == 0: 		# transition from state 0 to state 1
		squirtle.forward(70)
		squirtle.fillcolor("yellow")
		state_num = 1
	elif state_num == 1: 	# transition from state 1 to state 2
		squirtle.forward(70)
		squirtle.fillcolor("red")
		state_num = 2
	else:					# transition from state 2 to state 0
		squirtle.back(140)
		squirtle.fillcolor("green")
		state_num = 0


# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")


wn.listen()
wn.mainloop()