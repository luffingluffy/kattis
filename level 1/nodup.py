text = input().split()
unique_words = set()

for x in text:
    if x not in unique_words:
        unique_words.add(x)
    else:
        print("no")
        break

if len(text) == len(unique_words):
    print("yes")
