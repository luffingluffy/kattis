n, b = input().split()

value = {
	
	'A': (11, 11),
	'K': (4, 4),
	'Q': (3, 3),
	'J': (20, 2),
	'T': (10, 10),
	'9': (14, 0),
	'8': (0, 0),
	'7': (0,0)

}

score = 0

for i in range(4 * int(n)):
	card = input()
	if card[1] == b:
		score += value[(card[0])][0]
	else:
		score += value[(card[0])][1]

print(score)

# worst program ive wrote so far.. it is a literal manually-coded brute force program
# i'll need to revisit this to make it better

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
