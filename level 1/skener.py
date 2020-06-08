R, C, Zr, Zc = map(int, input().split())

for _ in range(R):
	x = input()
	# height multiplier
	for _ in range(Zr):
		# width multiplier
		print(''.join([i * Zc for i in x]))
