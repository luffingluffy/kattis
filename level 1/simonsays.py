N = int(input())

for _ in range(N):
	command = input()
	if "Simon says" in command:
		print(command[11:])
