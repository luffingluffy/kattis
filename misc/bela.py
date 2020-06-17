# worst code i've written... literal manually-coded brute force solution
# need to be improved/ rewritten

N, B = input().split()
sum = 0

for x in range(int(N) * 4):
    hand = input()

    if hand[1] == B:
        if hand[0] == 'J':
            sum += 20
        elif hand[0] == '9':
            sum += 14
        elif hand[0] == 'A':
            sum += 11
        elif hand[0] == 'K':
            sum += 4
        elif hand[0] == 'Q':
            sum += 3
        elif hand[0] == 'T':
            sum += 10
        elif hand[0] == '8':
            sum += 0
        elif hand[0] == '7':
            sum += 0

    elif hand[1] != B:
        if hand[0] == 'J':
            sum += 2
        elif hand[0] == '9':
            sum += 0
        elif hand[0] == 'A':
            sum += 11
        elif hand[0] == 'K':
            sum += 4
        elif hand[0] == 'Q':
            sum += 3
        elif hand[0] == 'T':
            sum += 10
        elif hand[0] == '8':
            sum += 0
        elif hand[0] == '7':
            sum += 0

print(sum)
