def seq3np1(n):
	""" Print the 3n+1 sequence from n, terminating when it reaches 1. """
	step = 0
	while n != 1:
		print(n, end=", ")
		if n % 2 == 0:
			n = n // 2
		else:
			n = n * 3 + 1
		step += 1
	print("{0}. Number of steps: {1}\n".format(n, step))


for i in range(1,100):
	seq3np1(i)