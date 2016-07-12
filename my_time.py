class MyTime:
	def __init__(self, hrs=0, mins=0, secs=0):
		""" 
		Create a MyTime object initialized to hrs, mins, secs.
		The values of mins and secs may be outside the range 0-59,
		but the resulting MyTime object wil lbe normalized.
		"""
		# Calculate total seconds to represent
		totalsecs = hrs*3600 + mins*60 + secs
		self.hours = totalsecs // 3600	# Split in h, m, s
		leftoversecs = totalsecs % 3600
		self.minutes = leftoversecs // 60
		self.seconds = leftoversecs % 60


	def __str__(self):
		return "{0:02}:{1:02}:{2:02}".format(self.hours, self.minutes, self.seconds)


	def increment(self, seconds):
		self.seconds += seconds

		while self.seconds >= 60:
			self.seconds -= 60
			self.minutes += 1

		while self.minutes >= 60:
			self.minutes -= 60
			self.hours += 1


	def to_seconds(self):
		""" Return the number of seconds represented by this instance. """
		return self.hours * 3600 + self.minutes * 60 + self.seconds


	def after(self, time2):
		""" Return True if I am strictly greater than time2. """
		return self.to_seconds() > time2.to_seconds()


	def __add__(self, other):
		return MyTime(0, 0, self.to_seconds() + other.to_seconds())

	def __sub__(self, other):
		return MyTime(0, 0, self.to_seconds() - other.to_seconds())



# Pure function, outside of the MyTime object
def add_time(t1, t2):
	secs = t1.to_seconds() + t2.to_seconds()
	return MyTime(0, 0, secs)


'''
current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
# print(done_time)
print("Done time: {0}".format(done_time))
# current_time.increment(500)
current_time.increment(13000) # To trigger the message
print("Current time: {0}".format(current_time))
if current_time.after(done_time):
	print("The bread will be done before it starts!")
'''

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
print(t1 + t2)
print(t2 - t1)