n = input().split()
money = 0

buying_power = {
	 
	 0: 3,
	 1: 2,
	 2: 1,

}

for x in range(len(n)):
	money += int(n[x]) * buying_power[x]

output = {
	
	0: "Copper",
	1: "Copper",
	2: "Estate or Copper",
	3: "Estate or Silver",
	4: "Estate or Silver",
	5: "Duchy or Silver",
	6: "Duchy or Gold",
	7: "Duchy or Gold",
	8: "Province or Gold",
}

print(output.get(money, "Province or Gold"))
