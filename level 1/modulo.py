x = [int(input()) for x in range(10)]
distinct = []

for i in x:
	a = i % 42
	if a not in distinct:
		distinct.append(a)

print(len(distinct))
