n, m = map(int, input().split())
a = min(n, m)

# pattern recognition of the probability
if n == m:
    print(n + 1)
else:
    for x in range(abs(n - m) + 1):
        a += 1
        print(a)
