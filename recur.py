def recurPower(base, exp):
	''' 	just a little recursive function to return an exponant.
		float or in in
		float or in returned
	'''

	if exp < 1:
		return 1
	else:
		return base * recurPower(base, exp - 1)

a = 5
b = 17

print recurPower(a,b)   	# use funtion
print a ** b		# test result





