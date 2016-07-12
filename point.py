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


	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)


	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)


	def __mul__(self, other):
		"""
		If the left operand is a Point, and Python assumes the right operand
		is also a Point, this computes the dot product.
		"""
		return self.x * other.x + self.y * other.y


	def __rmul__(self, other):
		"""
		If the left operand is a primitive type and the right operand is a Point,
		this does scalar multiplication.
		"""
		return Point(other * self.x, other * self.y)


	def reverse(self):
		(self.x, self.y) = (self.y, self.x)



# Polymorphic functions
def multadd(x, y, z):
	return x * y + z


def front_and_back(front):
	import copy
	back = copy.copy(front)
	back.reverse()
	print(str(front) + str(back))


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

p1 = Point(3, 4)
p2 = Point(5, 7)
# print(p1 + p2)
# print(p1 - p2)
# print(p1 * p2)
# print(2* p2)
print(multadd(2, p1, p2)) # Returns (11, 15)
print(multadd(p1, p2, 1)) # Returns 44
print(multadd(3, 2, 1))


my_list = [1, 2, 3, 4]
front_and_back(my_list)

front_and_back(p1)
