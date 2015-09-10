# odd.py
# return a Tuple that is a selection from an
# existing Tuple.
#
# Mark Addinall - Sept 2015
# MIT Computer Science - Python

def oddTuples(aTup):

	odd = True					# easier than modulus
	oddTups = ()					# empty tuple

	for x in aTup:
		if odd:
			oddTups = oddTups + (x,)	# we want 1,3,5,...,n
		odd = not odd				# flip the boolean
	return oddTups					# send it back to caller

t = ('I', 'am', 'a', 'test', 'tuple')

print oddTuples(t)

