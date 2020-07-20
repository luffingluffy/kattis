x = input()
days = 0
split = [x[i:i + 3] for i in range(0, len(x), 3)]

for i in split:
	if i[0] != 'P':
		days += 1
	
	if i[1] != 'E':
		days += 1
	
	if i[2] != 'R':
		days += 1

print(days)
