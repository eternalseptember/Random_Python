"""
Given set S = {1, 2, 3, ..., N}. Find two integers, A and B
(where A < B), from set S such that the value of A&B is the
maximum possible and also less than a given integer, K. In
this case, & represents the bitwise AND operator.

Input Format
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case as 2 space-
separated integers, N and K, respectively.
"""


t = 3
lines = ['5 2', '8 5', '2 2']

# t = int(input().strip())
for a0 in range(t):
	# n, k = input().strip().split(' ')
	n, k = lines[a0].strip().split(' ')
	n, k = int(n), int(k)

	s = list(range(1, n + 1))
	maxValue = 0

	for i in range(n - 1):
		a = s[i]
		for j in range(i + 1, n):
			b = s[j]
			result = a & b
			if (result > maxValue) and (result < k):
				maxValue = result

	print(maxValue)

