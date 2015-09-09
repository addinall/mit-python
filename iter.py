def iterPower(base, exp):
	''' 	just a little iterative function to return an exponant.
		float or in in
		float or in returned
	'''

	result = 1
	for i in range(1, exp + 1):
		result *= base	
		print("i == " + str(i))
		print("result == " + str(result))

	return result 

a = 5
b = 17

print iterPower(a,b)   	# use funtion
print a ** b		# test result





