c = float(input())
n = int(input())
cost = 0

for x in range(n):
    w, l = map(float, input().split())
    cost += w * l * c

print("%.7f" % cost)
