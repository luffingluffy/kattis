 n = [str(input()) for x in range(int(input()))]
last_digit = [x[-1] for x in n]
number = [x[0:-1] for x in n]
total = 0

for x in range(len(n)):
	total += int(number[x]) ** int(last_digit[x])

print(total)
