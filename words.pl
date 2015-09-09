# Find the longest substring that is in alphabetical order
# # from a supplied string as parameter.
#  Mark Addinall - MIT CompSci
#
def longest_word(s):
	'''	Traverse a string and return the longest
		sub-string contained that is in alphabetical
		order.  Return the FIRST in case of a tie,
		not the lexical winner.
		M. Addinall
		MIT - edX 6.001    '''

	# keep a data frame of the words found
	words=[]
	# and a string for the current word being built
	current = ''
	for ch in s:
		# if the current word is empty or the current
		# walkthrough char is in alphabetical order,
		# then continue building the current word

		if not current or ch >= current[-1]:
			current += ch
			print("ch -> " + ch)
			print("current -> " + current)
		else:
		# we have come to the end of a sequence of chars
		# in alphabetical order
		# push() the current word onto the data frame
		# and save the current ch in the current word

			print("pushing -> " + current)
			words.append(current)
			current = ch

	# OK, we have processed the last char, but we may
	# still have a word that need adding to the data frame
	# it the TAIL sequence were all in alphabetical order.
		
	if len(current) > 1:
		words.append(current)

	# option to sort the data frame
	# words.sort()
 	return max(words, key=len)


# test it
	
s = 'abcdefghijklmnopqrstuvwxyz'
s = 'slzscsllabjx'
print longest_word(s)

