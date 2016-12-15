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
		self.size = 0
		self.heap_array = []

		# Print functions use these queues, and not heap_array.
		self.print_queue = []
		self.level_order_queue = []


	def insert(self, root, data):
		new_node = Node(data)
		self.heap_array.append(new_node)
		self.size += 1

		"""
		print('\n')
		print('Heap details BEFORE inserting: {0}'.format(new_node))
		self.print_heap_array_details()
		"""

		if root is None:
			return new_node
		else:
			# In case new_node is a duplicate node, get its index here.
			# If parent_index is -1, then there's only one item.
			# The -1 index is the last item on the list.
			new_node_index = len(self.heap_array) - 1
			parent_index = self.get_parent_index(new_node_index)
			parent_node = self.heap_array[parent_index]

			if parent_node.left is None:
				parent_node.left = new_node
			else:
				parent_node.right = new_node

			self.check_min_and_heapify_up(new_node, new_node_index)

			"""
			print()
			print('Heap details AFTER inserting: {0}'.format(new_node))
			self.print_heap_array_details()
			"""

		return self.heap_array[0]


	def get_parent_index(self, node_index):
		# Only use this function if heap_array has been populated or sorted.
		# Due to duplicate nodes, changed this function to receive node_index.
		parent_index = (node_index - 1) // 2
		return parent_index


	def get_child_index(self, parent_index, node_dir):
		# node_dir = 0: left child
		# node_dir = 1: right child
		child_index = 2 * parent_index + 1 + node_dir
		return child_index


	def check_min_and_heapify_up(self, new_node, new_node_index):
		# used after inserting a new node
		parent_index = self.get_parent_index(new_node_index)

		if parent_index == -1:
			return

		parent_node = self.heap_array[parent_index]

		if parent_node.data > new_node.data:
			new_parent, new_par_index = self.heapify_up(new_node, new_node_index)
			self.check_min_and_heapify_up(new_parent, new_par_index)


	def heapify_up(self, child, child_index):
		# For a min-heap, when the parent is greater than the child.
		# Used after inserting a new node.

		# get the child's parent node, called 'node'
		node_index = self.get_parent_index(child_index)
		node = self.heap_array[node_index]
		node_left = node.left
		node_right = node.right
		child_left = child.left
		child_right = child.right

		# if node has a parent, update the node's parent to point to the child
		parent_index = self.get_parent_index(node_index)
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
		return child, node_index


	def remove(self, root):
		if len(self.heap_array) == 0:
			return None

		last_element = self.heap_array.pop()
		self.size -= 1

		if len(self.heap_array) == 0:
			return last_element
		else:
			# Get the last element and update its parent's pointer.
			last_elem_index = len(self.heap_array)
			last_elem_par_index = self.get_parent_index(last_elem_index)
			last_elem_par_node = self.heap_array[last_elem_par_index]

			if last_elem_par_node.left == last_element:
				last_elem_par_node.left = None
			else:
				last_elem_par_node.right = None
			# Save back to heap_array?
			self.heap_array[last_elem_par_index] = last_elem_par_node

			# Pop the first element, exchange left and right pointers,
			# insert last_element into top of heap array, then heapify downward.
			first_element = self.heap_array.pop(0)
			last_element.left, first_element.left = first_element.left, last_element.left
			last_element.right, first_element.right = first_element.right, last_element.right
			self.heap_array.insert(0, last_element)
			self.check_min_and_heapify_down(last_element, 0)

			return first_element


	def check_min_and_heapify_down(self, node, node_index):
		if node.left is None:
			return
		elif node.right is None:
			if node.left.data > node.data:
				new_child, new_child_index = self.heapify_down(node, node_index, node.left)
				self.check_min_and_heapify_down(new_child, new_child_index)
		else:
			# If bigger than both children, then switch with smaller of the two.
			if (node.left.data > node.data) and (node.left.data < node.right.data):
				new_child, new_child_index = self.heapify_down(node, node_index, node.left)
				self.check_min_and_heapify_down(new_child, new_child_index)
			elif (node.right.data > node.data) and (node.right.data < node.left.data):
				new_child, new_child_index = self.heapify_down(node, node_index, node.right)
				self.check_min_and_heapify_down(new_child, new_child_index)


	def heapify_down(self, node, node_index, child_node):
		# For a min-heap, when the parent is greater than the child.
		# Used after removing the root node.
		# Child_node is used to specify direction.

		# Return the new child and child_index


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


print('After all of the inserts are done...')
heap.print(root)


