import math
n = int(input())

def time(i, j, k):
	return i / (j * math.cos(math.radians(k)))

def height(a, b):
	return (a * time(x, v, ang) * math.sin(math.radians(b))) - ((1/2) * 9.81 * time(x, v, ang) ** 2)

for _ in range(n):
	v, ang, x, h1, h2 = map(float, input().split())

	if height(v, ang) > h1 + 1 and height(v, ang) < h2 - 1:
		print("Safe")
	
	else:
		print("Not Safe")
