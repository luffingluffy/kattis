n = int(input())
sum = 0

for x in range(n):
    q, y = map(float, input().split())
    sum += q * y

print('%.3f' % sum)
