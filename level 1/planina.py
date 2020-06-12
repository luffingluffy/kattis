import math
n = int(input())

def points(n):
    if n == 1:
        return 9
    else:
        return int((math.sqrt(points(n - 1)) * 2 - 1) ** 2)


print(points(n))
