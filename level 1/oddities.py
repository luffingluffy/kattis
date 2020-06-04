n = [int(input()) for i in range(int(input()))]

for x in n:
	if x % 2 == 0:
		print("{} is even".format(x))
	else:
		print("{} is odd".format(x))
