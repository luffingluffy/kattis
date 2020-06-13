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

# better way to solve
 
n = int(input())

while n != -1:
    distance = 0
    time_elapsed = 0
    for x in range(n):
        s, t = map(int, input().split())
        distance += s * (t - time_elapsed)
        time_elapsed = t
    print(str(distance) + " miles")
    n = int(input())
