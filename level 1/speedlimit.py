n = int(input())
s = []
t = []
distance = 0

while n != -1:
    for x in range(n):
        a, b = map(int, input().split())
        s.append(a)
        t.append(b)
        if x == 0:
            distance += s[0] * t[0]
        else:
            distance += s[x] * (t[x] - t[x - 1])
    print(str(distance) + " miles")
    distance = 0
    s.clear()
    t.clear()
    n = int(input())
