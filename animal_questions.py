from trees import Tree

def yes(ques):
	ans = input(ques).lower()
	return ans[0] == "y"

def animal():
	# Start with a singleton
	root = Tree("bird")

	# Loop until the user quits
	while True:
		print()
		if not yes("Are you thinking of an animal? "): break

		# Walk the tree
		tree = root
		while tree.left is not None:
			prompt = tree.cargo + "? "
			if yes(prompt):
				tree = tree.right
			else:
				tree = tree.left

		# Make a guess
		guess = tree.cargo
		prompt = "Is it a " + guess + "? "
		if yes(prompt):
			print("I rule!")
			continue

		# Get new information
		prompt = "What is the animal\'s name? "
		animal = input(prompt)
		prompt = "What question would distinguish a {0} from a {1}? "
		question = input(prompt.format(animal, guess))

		# Add new information to the tree
		tree.cargo = question
		prompt = "If the animal were {0} the answer would be? "
		if yes(prompt.format(animal)):
			tree.left = Tree(guess)
			tree.right = Tree(animal)
		else:
			tree.left = Tree(animal)
			tree.right = Tree(guess)



