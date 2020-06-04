current = [int(x) for x in input().split()]
#converts str(input()) into int
valid = [1,1,2,2,2,8]
difference = []
#creates a list to contain the difference 

for i in range(len(valid)):
	difference.append(valid[i]-current[i])


print(' '.join([str(a) for a in difference]))
