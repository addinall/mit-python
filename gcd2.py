# Greatest Common denominator - recursive
#
# Mark Addinall - September 2015
# MIT Computer Science - Python

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


print gcd(17,12)



