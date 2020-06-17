import math
a, i = map(int, input().split())
c = a * i

while math.ceil(c / a) == i:
    c -= 1

print(c + 1)
