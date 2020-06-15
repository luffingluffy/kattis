l, x = map(int,input().split())
n = 0
d = 0

for i in range(x):
    z = input().split()
    # no. of times a group is denied entry
    if z[0] == "enter":
        if n + int(z[1]) > l:
            d += 1
        # no. of people entering that wasn't denied
        else:
            n += int(z[1])
    # no. of people leaving
    else:
        n -= int(z[1])

print(d)
