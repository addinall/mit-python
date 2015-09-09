def lenIter(aStr):
	i = 0
	if not aStr:
		return i
	for c in aStr:
		i += 1

	return i

print lenIter("Addinall")
print lenIter("")

