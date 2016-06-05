'''
def square(num):
	print (num*num)

for x in range (1,11):
	square(x)
'''

def print_multiples(n, high):
	for i in range(1, high+1):
		print (n*i, end="\t")
	print()

def print_mult_table(high):
	for i in range(1, high+1):
		print_multiples(i, high)


def print_multi_table(high):
	for i in range (1, high+1):
		for j in range (1, high+1):
			print(i*j, end="\t") # print each number here
		print() # print blank line for new row


print_multi_table(10)
