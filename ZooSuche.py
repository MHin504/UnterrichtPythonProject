def binary_search(items, gesucht):
	index = -1
	anfang = 0
	ende = len(items) - 1
	gefunden = False

	while anfang <= ende and not gefunden:
		mitte = (anfang + ende) // 2
		tier = items[mitte]

		if tier == gesucht:
			index = mitte
			gefunden = True

		elif tier < gesucht:
			anfang = mitte + 1
		else:
			ende = mitte - 1
	return index

zoo_sortiert = [ '🐍', '🐒','🐘', '🐧','🐫','🐱','🐶', '🦉', '🦎']

for c in zoo_sortiert:
	print(f"{c} -> {ord(c)}")
## test -- suche den 🐘
print(binary_search(zoo_sortiert, '🐘'))