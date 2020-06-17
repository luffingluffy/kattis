import math
h, v = map(int, input().split())
hypotenuse = math.ceil(h / math.sin(math.radians(v)))

print(hypotenuse)
