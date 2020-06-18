order = []

for x in range(5):
    blimp = input()
    if "FBI" in blimp:
        order.append(str(x + 1))

output = " ".join(order)

if not output:
    print("HE GOT AWAY!")
else:
    print(output)
