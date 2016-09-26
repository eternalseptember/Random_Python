class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)


def print_list(node):
	while node is not None:
		print(node, end=" ")
		node = node.next
	print()


def print_backward(list):
	if list is None: return
	head = list
	tail = list.next
	print_backward(tail)
	print(head, end=" ")


def remove_second(list):
	if list is None: return
	try:
		first = list
		second = list.next
		# Make the first node refer to the third
		first.next = second.next
		# Separate the second node from the rest of the list
		second.next = None
		return second
	except AttributeError:
		return


def print_backward_nicely(list):
	print("[", end=" ")
	try: 
		print_backward(list)
		print("]")
	except AttributeError:
		print("]")
		return





'''
node = Node("test")
print(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print_list(node1)
print_backward_nicely(node1)
removed = remove_second(node1)
print_list(removed)
print_list(node1)
'''

remove_second([]) # attribute error: 'list' object has no attribute 'next
node4 = Node(4)
remove_second(node4) # attribute error: 'nonetype' object has no attribute 'next'