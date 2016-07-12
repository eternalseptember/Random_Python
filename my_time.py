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
		return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)


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


'''
# Pure function, outside of the MyTime object
def add_time(t1, t2):
	h = t1.hours + t2.hours
	m = t1.minutes + t2.minutes
	s = t1.seconds + t2.seconds

	if s >= 60:
		s -= 60
		m += 1

	if m >= 60:
		m -= 60
		h += 1

	sum_t = MyTime(h, m, s)
	return sum_t
'''


'''
time1 = MyTime(11, 59, 30)
print(time1)
'''

current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
print(done_time)
current_time.increment(500)
print(current_time)