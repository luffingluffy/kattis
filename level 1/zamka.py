l = int(input())
d = int(input())
x = int(input())

while True:
	sum_digitsl = sum(int(i) for i in str(l))
	if sum_digitsl == x:
		print(l)
		break
	else:
		l += 1

while True:
	sum_digitsd = sum(int(j) for j in str(d))
	if sum_digitsd == x:
		print(d)
		break
	else:
		d -= 1
