import math

def probability(b):
	
	if b == 0:
		return 1

	def birthday(x, y):
		return 1 - (math.factorial(y) / (math.factorial(y - x) * y ** x))

	return birthday(a - ((b - 1) * 2), 366 - b) * probability(b - 1)

# a = no. of people in group, b = no. of pairs with matching birthdays 
a, b = map(int, input().split())
print(probability(b))
