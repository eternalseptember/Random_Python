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
		self.level_order_queue = []


	def insert(self, root, data):
		new_node = Node(data)
		self.heap_array.append(new_node)

		if root is None:
			return new_node
		else:
			# if parent_index is -1... then there's only one item...
			# the -1 index is the last item on the list
			parent_index = self.get_parent(new_node)
			parent_node = self.heap_array[parent_index]

			if parent_node.left is None:
				parent_node.left = new_node
			else:
				parent_node.right = new_node

			print()
			print('calling check function at: {0}'.format(new_node))
			print('current heap:', end=' ')
			self.print(root)
			# make this function heapify upward
			self.check_min_and_heapify(new_node)

		return self.heap_array[0]



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


	def check_min_and_heapify(self, node):
		# make this function heapify upward
		parent_index = self.get_parent(node)
		print('node: {0}  parent_index: {1}'.format(node, parent_index))

		if parent_index == -1:
			return

		parent_node = self.heap_array[parent_index]

		if parent_node.data > node.data:
			print('parent node is larger. Parent: {0}  Child: {1}'.format(parent_node, node))
			#new_root, new_child = self.heapify(node, parent_node)
			self.heapify(node, parent_node)
			#self.check_min_and_heapify(new_child)
		else:
			return


	def heapify(self, child_node, node):
		node_index = self.heap_array.index(node)
		left_child = node.left
		right_child = node.right
		child_index = self.heap_array.index(child_node)
		child_left_child = child_node.left
		child_right_child = child_node.right

		print('parent-index: {0}  left-child: {1}  right-child: {2}'.format(node_index, left_child, right_child))
		print('child-index: {0}  child-left: {1}  child-right: {2}'.format(child_index, child_left_child, child_right_child))
		print('now swap...')

		# update the child node to become the new parent node
		if node.left == child_node:
			# print('heapify condition 1')
			child_node.left = node
			child_node.right = right_child
		else:
			# print('heapify condition 2')
			child_node.right = node
			child_node.left = left_child
		self.heap_array[node_index] = child_node

		print('new parent: {0}  child-left: {1}  child-right: {2}'.format(child_node, child_node.left, child_node.right))


		# if applicable, change node's parent to point to the child node
		parent_index = self.get_parent(child_node)
		# print('parent index: {0}'.format(parent_index))
		if parent_index > -1:
			parent = self.heap_array[parent_index]
			print('parent_index: {0}  parent: {1}'.format(parent_index, parent))
			if parent.left == node:
				print('node: {0}  node-left: {1}  node-right: {2}'.format(node, ))
				parent.left = child_node
			else:
				parent.right = child_node
			self.heap_array[parent_index] = parent

		# node is now the new child node
		node.left = child_left_child
		node.right = child_right_child
		self.heap_array[child_index] = node


		child = self.heap_array[child_index]
		print('new child: {0}  root-left: {1}  root-right: {2}'.format(child, child.left, child.right))
		print('updated level-order:', end=' ')
		root = self.heap_array[0]
		self.print(root)
		
		return root, child


	def get_parent(self, node):
		""" Only use this function if heap_array has been populated or sorted. """
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

print()
#heap.print(root)
#heap.print_heap_array_details()
