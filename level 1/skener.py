R, C, Zr, Zc = map(int, input().split())

for _ in range(R):
	x = input()
	for _ in range(Zr):
		print(''.join([i * Zc for i in x]))
