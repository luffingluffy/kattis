n = int(input())

for x in range(n):
    b, p = map(float, input().split())
    bpm = 60 * b / p
    print("{:.4f} {:.4f} {:.4f}".format(bpm - 60/p, bpm, bpm + 60/p))
