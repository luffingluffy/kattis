d, m = map(int, input().split())

months	= {
	
	0 : (0),
	1 : (31),
	2 : (28),
	3 : (31),
	4 : (30),
	5 : (31),
	6 : (30),
	7 : (31),
	8 : (31),
	9 : (30),
	10 : (31),
	11 : (30),

}

day = {

	0 : ('Wednesday'),
	1 : ('Thursday'),
	2 : ('Friday'),
	3 : ('Saturday'),
	4 : ('Sunday'),
	5 : ('Monday'),
	6 : ('Tuesday'),

}

for x in range(m):
	d += months[(x)] 


print(day[(d % 7)])
