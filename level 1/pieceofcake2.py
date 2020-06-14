n, h, v = map(int, input().split())
areas = []
areas.append(h * v)
areas.append(h * (n - v))
areas.append((n - h) * v)
areas.append((n - h) * (n - v))

print(max(areas) * 4)
