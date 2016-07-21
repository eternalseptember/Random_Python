class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.cargo)


def total(tree):
	if tree is None: return 0
	return total(tree.left) + total(tree.right) + tree.cargo


def print_tree_preorder(tree):
	if tree is None: return
	print(tree.cargo, end=" ")
	print_tree_preorder(tree.left)
	print_tree_preorder(tree.right)


def print_tree_postorder(tree):
	if tree is None: return
	print_tree_postorder(tree.left)
	print_tree_postorder(tree.right)
	print(tree.cargo, end=" ")


def print_tree_inorder(tree):
	if tree is None: return
	print_tree_inorder(tree.left)
	print(tree.cargo, end=" ")
	print_tree_inorder(tree.right)


def print_tree_indented(tree, level=0):
	if tree is None: return
	print_tree_indented(tree.right, level+1)
	print(" " * level + str(tree.cargo))
	print_tree_indented(tree.left, level+1)



tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
print_tree_preorder(tree)
print()
print_tree_postorder(tree)
print()
print_tree_inorder(tree)
print()
print_tree_indented(tree)