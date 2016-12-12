"""
Heap implemented with a binary tree.
For experimental/educational purposes only. Possibly incomplete
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)

	def __eq__(self, other):
		try:
			return ((self.data == other.data) and
					(self.left == other.left) and
					(self.right == other.right))
		except AttributeError:
			return False


class Heap:
	def __init__(self, type=min):
		self.type = type
		self.heap_array = []

		# Print functions use these queues, and not heap_array.
		self.print_queue = []
		self.level_order_queue = []


	def insert(self, root, data):
		new_node = Node(data)
		self.heap_array.append(new_node)

		print('\n')
		print('Heap details BEFORE inserting: {0}'.format(new_node))
		self.print_heap_array_details()


		if root is None:
			return new_node
		else:
			# if parent_index is -1... then there's only one item...
			# the -1 index is the last item on the list
			parent_index = self.get_parent_index(new_node)
			parent_node = self.heap_array[parent_index]

			if parent_node.left is None:
				parent_node.left = new_node
			else:
				parent_node.right = new_node

			self.check_min_and_heapify(new_node)

			print()
			print('Heap details AFTER inserting: {0}'.format(new_node))
			self.print_heap_array_details()

		return self.heap_array[0]


	def heapify_up(self, child):
		# For a min-heap, when the parent is greater than the child.
		# Used after inserting a new node.

		# get the child's parent node, called 'node'
		node_index = self.get_parent_index(child)
		node = self.heap_array[node_index]
		node_left = node.left
		node_right = node.right
		child_index = self.heap_array.index(child)
		child_left = child.left
		child_right = child.right

		# if node has a parent, update the node's parent to point to the child
		parent_index = self.get_parent_index(node)
		if parent_index > -1:
			parent = self.heap_array[parent_index]
			if parent.left == node:
				parent.left = child
			else:
				parent.right = child
			self.heap_array[parent_index] = parent

		# swap node and child
		if node.left == child:
			child.left = node
			child.right = node_right
		else:
			child.right = node
			child.left = node_left
		self.heap_array[node_index] = child

		node.left = child_left
		node.right = child_right
		self.heap_array[child_index] = node

		# 'child' has been switched with its parent
		return child


	def check_min_and_heapify(self, new_node):
		# used after inserting a new node
		parent_index = self.get_parent_index(new_node)

		if parent_index == -1:
			return

		parent_node = self.heap_array[parent_index]

		if parent_node.data > new_node.data:
			new_parent = self.heapify_up(new_node)
			self.check_min_and_heapify(new_parent)
		else:
			return


	def get_parent_index(self, node):
		""" Only use this function if heap_array has been populated or sorted. """
		child_index = self.heap_array.index(node)
		parent_index = (child_index - 1) // 2
		return parent_index


	# Functions below here are "helper" functions to inspect what is in the heap.
	# Only print_heap_array_details should use heap_array.
	# Everything else uses print_queue or level_order_queue.
	def print(self, root):
		# This was a function for testing purposes.
		self.print_queue.clear()
		self.level_order(root)
		for i in self.print_queue:
			print(i.data, end=' ')
		print()


	def level_order(self, root):
		# This is used to convert binary tree heap to array representation.
		# Clear the print_queue before calling level_order.
		if len(self.print_queue) == 0:
			self.print_queue.append(root)

		if root.left is not None:
			self.print_queue.append(root.left)
			self.level_order_queue.append(root.left)
		if root.right is not None:
			self.print_queue.append(root.right)
			self.level_order_queue.append(root.right)

		if len(self.level_order_queue) > 0:
			next_node = self.level_order_queue.pop(0)
			self.level_order(next_node)


	def print_heap_array_details(self):
		""" Assumes the heap_array is already filled and sorted. """
		for i in self.heap_array:
			print('Node: {0}  Left: {1}  Right: {2}'.format(i.data, i.left, i.right))




# test case
# original list: [5, 9, 3, 4, 6, 2, 7, 1, 8, 5]
elements_in = [5, 9, 3, 4, 6, 2, 7, 1, 8, 5]

heap = Heap(min)
root = None

for i in elements_in:
	root = heap.insert(root, i)

print()
print('After all of the inserts are done...')
heap.print(root)