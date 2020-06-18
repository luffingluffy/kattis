# i did this through brute-force,, i'll try to do it by recursion tomorrow

pos = 1

for x in input():
	if x == "A" and pos == 1:
		pos += 1
	elif x == "A" and pos == 2:
		pos -= 1
	elif x == "B" and pos == 2:
		pos += 1
	elif x == "B" and pos == 3:
		pos -= 1
	elif x == "C" and pos == 1:
		pos += 2
	elif x == "C" and pos == 3:
		pos -= 2

print(pos)
