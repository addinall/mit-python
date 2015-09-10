# Just some little base number swaps
#
#
# Mark Addinall - September 2015
# MIT Computer Science - Python

# dec to bin
num = 302 
result = ''
while num > 0:
	result = str(num % 2) + result
	num = num / 2
print result

# fractional numbers
# 
# If there in no INTEGER p such that x*(2^p) is
# a whole number, then internal representation is
# always an APPROXIMATION
#

# dec to oct
num = 302 
result = ''
while num > 0:
	result = str(num % 8) + result
	num = num / 8 
print result

