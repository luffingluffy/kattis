results = []

for x in range(5):
	sum = 0
	score = map(int, input().split())
	for i in score:
		sum += i
	results.append(sum)

winner = max(results)
print("{} {}".format(results.index(winner) + 1, winner))
