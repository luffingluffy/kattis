x = int(input())
n = int(input())
balance = x

for i in range(n):
	balance += x - int(input())

print(balance)
