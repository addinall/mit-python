def lenRecur(aStr):
	if not aStr:
		return 0
	return 1 + lenRecur(aStr[1:])

print lenRecur("addinall")
print lenRecur("")


