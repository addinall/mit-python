# Use a recursive algorithm to test if
#    char is in aStr
#
# Mark Addinall - September 2015
# MIT Computer Science - Python

def isIn(char, aStr):
	''' 	binary search of an ordered list
		another lab question in the use
		of recursion '''

	if not aStr:
		return False				# why test NULLs?

	node = int(len(aStr)/2)				# get a binary chop
	print(aStr)
	print('node == ' + str(node))
	print('char == ' + char)
	print('string[node] == ' + aStr[node])

	if aStr[node] == char:
		return True				# did we find it?  Good.  Exit
	elif node == 0:
		return False 				# not found and run out of string!
	elif aStr[node] < char:			
		return(isIn(char, aStr[node:]))		# search in the top half
	elif aStr[node] > char:
		return(isIn(char, aStr[0:node])) 	# search in the bottom half

# test the function
		
if isIn('e','abcdefghijklm') == True:
	print('Found 1')
else:
	print('NOT Found 1')

if isIn('e','abcdfghijklm'):
	print('Found 2')
else:
	print('NOT Found 2')

if isIn('e',''):
	print('Found 3')
else:
	print('NOT Found 3')


