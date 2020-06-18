l, r = map(int, input().split())

if l == r:
    if l == 0 and r == 0:
        print("Not a moose")
    else:
        print("Even %i" % (l * 2))
elif l > r:
    print("Odd %i" % (l * 2))
else:
    print("Odd %i" % (r * 2))
