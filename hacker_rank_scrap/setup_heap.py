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
			return (self.data == other.data) and (self.left == other.left) and (self.right == other.right)
		except AttributeError:
			return False


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
			else:
				self.heap_array.clear()
				self.level_order(root)
				self.heap_array.append(new_node)
				parent_index = self.get_parent(new_node)
				parent_node = self.heap_array[parent_index]
				if parent_node.left is None:
					parent_node.left = new_node
				else:
					parent_node.right = new_node

				# save the changed node
				self.heap_array[parent_index] = parent_node

				# probably check and heapify next


		return root


	def remove_min(self, root):
		if root is None:
			return None

		left_child = root.left
		right_child = root.right

		# the following node and the root should be the same thing
		node = self.heap_array.pop(0)

		last_node = self.heap_array[-1]
		last_node_parent_index = self.get_parent(last_node)
		last_node_parent = self.heap_array[last_node_parent_index]

		if last_node_parent.left == last_node:
			last_node_parent.left = None
		else:
			last_node_parent.right = None

		# root is last_node
		root = self.heap_array.pop()
		root.left = left_child
		root.right = right_child

		self.heap_array.clear()
		self.level_order(root)

		# check and heapify
		self.check_min_and_heapify(root)

		return node, root


	def check_min_and_heapify(self, root):
		if (root.left is None) and (root.right is None):
			return
		# the left node should be filled
		elif (root.right is None):
			if root.left.data < root.data:
				root, lower_node = self.heapify(root, root, root.left)
				return self.check_min_and_heapify(lower_node)
			else:
				return
		else:
			smaller_child = None
			if root.left.data < root.right.data:
				smaller_child = root.left
			else:
				smaller_child = root.right

			if smaller_child.data < root.data:
				root, lower_node = self.heapify(root, root, smaller_child)
				return self.check_min_and_heapify(lower_node)
			else:
				return


	def heapify(self, root, node, child_node=None):
		parent = self.get_parent(node)
		left_child = node.left
		right_child = node.right
		child_left_child = child_node.left
		child_right_child = child_node.right

		if parent > -1:
			if parent.left == node:
				parent.left = child_node
			else:
				parent.right = child_node

		if node.left == child_node:
			child_node.left = node
			child_node.right = right_child
		else:
			child_node.right = node
			child_node.left = left_child


		node.left = child_left_child
		node.right = child_right_child

		# the heap_array needs to be redone
		self.heap_array.clear()
		self.level_order(root)
		return root, node


	def get_parent(self, node):
		""" Only use this function if heap_array has been sorted. """
		child_index = self.heap_array.index(node)
		parent_index = (child_index - 1) // 2
		return parent_index


	def level_order(self, root):
		""" This is used to convert binary tree heap to array representation. """
		if len(self.heap_array) == 0:
			self.heap_array.append(root)

		if root.left is not None:
			self.heap_array.append(root.left)
			self.level_order_queue.append(root.left)
		if root.right is not None:
			self.heap_array.append(root.right)
			self.level_order_queue.append(root.right)

		if len(self.level_order_queue) > 0:
			next_node = self.level_order_queue.pop(0)
			self.level_order(next_node)


	def print(self, root):
		""" This was a function for testing purposes. """
		self.heap_array.clear()
		self.level_order(root)
		for i in self.heap_array:
			print(i.data, end=' ')
		print()


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

#heap.print(root)
heap.print_heap_array_details()
