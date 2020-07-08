def points(x):
	
	cardcount = []
	t = x.count("T")
	g = x.count("G")
	c = x.count("C")

	def cardval(x):
		return t ** 2 + g ** 2 + c ** 2

	def setval(x):
		cardcount.append(t)
		cardcount.append(g)
		cardcount.append(c)
		return min(cardcount) * 7

	return cardval(x) + setval(x)

print(points(list(input())))
