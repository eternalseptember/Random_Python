class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None

	def print_backward(self):
		print("[", end=" ")
		if self.head is not None:
			self.head.print_backward()
		print("]")

	def add_first(self, cargo):
		node = Node(cargo)
		node.next = self.head
		self.head = node
		self.length += 1


class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)

	def print_backward(self):
		if self.next is not None:
			tail = self.next
			tail.print_backward()
		print(self.cargo, end=" ")



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node1.next = node2
node2.next = node3

linkedlist1 = LinkedList()
linkedlist1.add_first(node1)
linkedlist1.print_backward()
linkedlist1.add_first(node2)
linkedlist1.print_backward()
linkedlist1.add_first(node3)
linkedlist1.print_backward()
