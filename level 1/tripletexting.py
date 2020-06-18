s = input()

index = int(len(s) / 3)

if s[:index] == s[-index:]:
	print(s[:index])
elif s[:index] == s[index:(index * 2)]:
	print(s[:index])
else:
	print(s[index:(index * 2)])
