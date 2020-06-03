long_name = input().split('-')
first_letter = [x[0] for x in long_name]
short_name = ''.join(first_letter)

print(short_name)
