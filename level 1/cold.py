n = int(input())
temperature = [int(x) for x in input().split()]
output = 0

for i in range(n):
	if temperature[i] < 0:
		output += 1

print(output)
