s, t, n = map(int, input().split())
d = input().split()
b = input().split()
c = input().split()
duration = 0
duration += s

for i in range(n):
	duration += int(d[i])
	if duration < int(c[i]):
		duration += int(c[i]) - duration
	else:
		duration += (duration % int(c[i]))
	duration += int(b[i])

duration += int(d[-1])

if duration <= t:
	print('yes')
else:
	print('no')
