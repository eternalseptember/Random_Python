class Point:
	""" Point class represents and manipulates x,y coords. """
	def __init__(self, x=0, y=0):
		""" Create a new point at the origin. """
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	def midpoint(self, target):
		mx = (self.x + target.x)/2
		my = (self.y + target.y)/2
		return Point(mx, my)

	def same_coordinates(self, target):
		return (self.x == target.x) and (self.y == target.y)

'''
p = Point(3, 4)
q = Point(5, 12)
r = p.midpoint(q)

# used to be print("({0}, {1})".format(p.x, p.y))
print(p)
print(p.distance_from_origin())
print(q)
print(q.distance_from_origin())
print(r)

p1 = Point(3, 4)
p2 = Point(3, 4)
same = p1.same_coordinates(p2)
print(same)
'''