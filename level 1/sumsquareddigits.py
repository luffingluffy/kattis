P = int(input())

for x in range(P):
	K, b, n = map(int, input().split())
	ssd = 0
	
	while n > 0:
		ssd += (n % b) ** 2
		n //= b
	
	print(K, ssd)
