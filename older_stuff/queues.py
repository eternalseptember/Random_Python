class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)



class Queue:
	def __init__(self):
		self.length = 0
		self.head = None

	def is_empty(self):
		return self.length == 0

	def insert(self, cargo):
		node = Node(cargo)
		if self.head is None:
			# If list is empty, the new node goes first
			self.head = node
		else:
			# Find the last node in the list
			last = self.head
			while last.next:
				last = last.next
			# Append the new node
			last.next = node
		self.length += 1

	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length -= 1
		return cargo



class ImprovedQueue:
	def __init__(self):
		self.length = 0
		self.head = None
		self.last = None

	def is_empty(self):
		return self.length == 0

	def insert(self, cargo):
		node = Node(cargo)
		if self.length == 0:
			# If list is empty, the new node is head and last
			self.head = self.last = node
		else:
			# Find the last node
			last = self.last
			# Append the new node
			last.next = node
			self.last = node
		self.length += 1

	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.last = None
		return cargo


class PriorityQueue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return not self.items

	def insert(self, item):
		self.items.append(item)

	def remove(self):
		maxi = 0
		for i in range(1, len(self.items)):
			if self.items[i] > self.items[maxi]:
				maxi = i
		item = self.items[maxi]
		del self.items[maxi]
		return item


'''
q = PriorityQueue()
for num in [11, 12, 14, 13]:
	q.insert(num)

while not q.is_empty():
	print(q.remove())
'''