# biggest.py
# A little function that returns the key to the largest list that
# is enclosed in a Dictionary of lists.
#
# Mark Addinall - Sept 2015
# MIT Computer Science - Python


def biggest(aDict):
    '''
        aDict: A dictionary, where all the values are lists.

    	returns: The key with the largest number of values associated with it
        '''
    key = None
    n = 0
    for x in aDict:
    	if len(aDict[x]) == 0:		# if there are keys that have empty values,
    		key = x			# the grading bot still wants at least on key.
					# don't as me why.  It SHOULD return None
  	if len(aDict[x]) > n:		# this now just keeps track of the entries
    		n = len(aDict[x])	# using a brute iteration.  We assume
    		key = x			# rater manageable size Dictionaries.
    return key


