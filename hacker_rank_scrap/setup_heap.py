"""
Heap implemented with a binary tree.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


class Heap:
	def __init__(self, type=min):
		self.type = type
		self.heap_array = []
		self.level_order_queue = []

	def insert(self, root, data):
		new_node = Node(data)

		if root is None:
			return new_node
		else:
			if root.left is None:
				root.left = new_node
			elif root.right is None:
				root.right = new_node
			# probably need a queue to specify the next position
			# check if the heap is sorted

		return root


	def check_min(self, root):
		# if only one node, then in min-heap state
		if (root.left is None) and (root.right is None):
			return True
		elif (root.left.data < root.data) or (root.right.data < root.data):
			return False
		# this may need to be recursive
		else:
			return True


	def heapify(self, root):
		if self.type == min:
			# switch nodes so that smaller value is on top
		else:
			# switch so that bigger value is on top

		# the heap_array needs to be redone
		self.heap_array.clear()


	def level_order(self, root):
		""" This is used to convert binary tree heap to array representation. """
		if len(self.heap_array) == 0:
			self.heap_array.append(root.data)

		if root.left is not None:
			self.heap_array.append(root.left.data)
			self.level_order_queue.append(root.left)
		if root.right is not None:
			self.heap_array.append(root.right.data)
			self.level_order_queue.append(root.right)

		if len(self.level_order_queue) > 0:
			next_node = self.level_order_queue.pop(0)
			self.level_order(next_node)


	def print(self, root):
		self.heap_array.clear()
		self.level_order(root)
		print(self.heap_array)


elements_in = [5, 9, 3, 4, 6, 2, 7, 1, 8, 5]

heap = Heap(min)
root = None

for i in elements_in:
	root = heap.insert(root, i)
	heap.print(root)

