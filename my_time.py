class MyTime:
	def __init__(self, hrs=0, mins=0, secs=0):
		""" Create a MyTime object initialized to hrs, mins, secs. """
		self.hours = hrs
		self.minutes = mins
		self.seconds = secs

	def __str__(self):
		return "It is {0}:{1}:{2}.".format(self.hours, self.minutes, self.seconds)


time1 = MyTime(11, 59, 30)
print(time1)