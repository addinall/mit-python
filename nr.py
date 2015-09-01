# Newton - Raphson Approximation
#  Mark Addinall - MIT CompSci
#
# General approximation algorithm to find the roots of 
# a polynomial in one variable
#
#                 n        n-1
#	p(x) = a x  + a   x    + ... + a x + a
#               n      n-1              1     0
#
# Want to find r such that p(r) = 0
#
# eg., to find the square root of 24, find the root of
#
#      p(x) = x^2 - 24
#
#
# Newton showed that if g is an approximation to the root, then
#
#      g - p(g)/p'(g)
#
# is a better approximation, where p' is a derivitive of p.
#
# - simple case:   	cx^2 + k
# - first derivative:	2cx
# - so if the polynomial is x^2 + k, then derivative is 2x
# - Newton - Raphson say that given a guess g for root,
#   a better guess is
#
#			g - (g^2 + k)/ 2g
#
#

epsilon = 0.01
y = 1234567890.0
guess = y/2.0
counter = 0 

while abs(guess*guess - y) >= epsilon:
	guess = guess - (((guess**2) - y) / (2 * guess))
	counter += 1
	print('count is : ' + str(counter) + ' Guess is : ' + str(guess))

print('Square root of ' + str(y) + ' is about ' + str(guess))




