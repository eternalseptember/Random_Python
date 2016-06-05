import math

def f(r):
	"""Return (circumference, area) of a circle of radius r. """
	c = 2 * math.pi * r
	a = math.pi * r * r
	return (c, a)


(circum, area) = f(3)
print("The circumference is {0:.2f} and the area is {1:.2f}.".format(circum, area))

'''
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print (julia[2])

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print (julia)
'''