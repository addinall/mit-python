# ask the user to guess a SECRET number that the computer
# will magically guess!  Simple demonstration of binary searching

valid_input = 'hlc'
ch = ''
high = 100
low = 0
print 'Please think of a number between 0 and 100!'

finished = False
while not finished:
	ans = (high + low) / 2
	print('Is your secret number ' + str(ans) + '?')

	ch = raw_input(	"Enter 'h' to indicate the guess is too high.  Enter 'l' to indicate the guess is too low.  Enter 'c' to indicate I guessed correctly. ")

	while not (ch in valid_input):
		print 'Sorry, I did not understand your input.'
		print('Is your secret number ' + str(ans) + '?')
		ch = raw_input(	"Enter 'h' to indicate the guess is too high.  Enter 'l' to indicate the guess is too low.  Enter 'c' to indicate I guessed correctly. ")
	# wend
	if ch == 'c':
		finished = True
	elif ch == 'l':
		low = ans
	else:
		high = ans
# wend

# should have a guess now
print("Game over. Your secret number was: " + str(ans))



