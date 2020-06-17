n = int(input())
at_bat = map(int, input().split(" "))
num = 0

for x in at_bat:
    if x == -1:
        n -= 1
    else:
        num += x

print(num / n)
