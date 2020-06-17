import collections

xlist = []
ylist = []

for x in range(3):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)

# counts the frequency of elements in the list
xcount = collections.Counter(xlist)
ycount = collections.Counter(ylist)

# sort the list according to the key (counter: increasing frequency) and get the least frequent number
xcoord = sorted(xlist, key=xcount.get)[0]
ycoord = sorted(ylist, key=ycount.get)[0]

print(xcoord, ycoord)
