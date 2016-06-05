from point import Point
import copy

class Rectangle:
	""" A class to manufacture rectangle objects """
	def __init__(self, posn, w, h):
		""" Initialize rectangle at posn, with width w, height h """
		self.corner = posn
		self.width = w
		self.height = h

	def __str__(self):
		return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

	def grow(self, delta_width, delta_height):
		self.width += delta_width
		self.height += delta_height

	def move(self, dx, dy):
		self.corner.x += dx
		self.corner.y += dy


box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100,80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)

box2 = copy.deepcopy(box)
print("box: ", box2)

r = Rectangle(Point(10,5), 100, 50)
print(r)
r.grow(25, -10)
print(r)
r.move(-10, 10)
print(r)