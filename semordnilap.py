# Is one string the reverse of another?
# exercize in recursion and slicing variables
#
#
# Mark Addinall - September 2015
# MIT Computer Science - Python

def semordnilap(str1, str2):

	''' 	strings are not equal
		strings are greater than one character
		function IS case sensitive
		returns boolean '''
	
	if not str1 and not str2:
		return True			# if BOTH are null, we have reduced them
						# all other CHARS must have been equal
						# by inductive reasoning

	if (len(str1) != len(str2)):		# if the strings are now two different
		return False			# lengths now, the CAN NOT be semordnilaps
						# by mathematical induction

	if str1[0] != str2[-1]:			# if the first char of first string is NOT
		return False			# equal to the last char of the second string,
						# then they ARE NOT semordnilaps
	else:
		return semordnilap(str1[1:],str2[:-1])
						# so far, so good.  Chop the string
						# and carry on


#test it


print semordnilap('Mark','Addinall')			# FALSE
print semordnilap('desserts','stressed')		# TRUE
print semordnilap('desserts','streabitbiggerssed')	# FALSE


