# x = 1234567890 this would take about a year using an exhaustive search with these epsilons.  Sub second using the binary search in 57 guesses.


x = 25
epsilon = 0.0001
step = epsilon**2
guesses = 0
ans = 0.0
low = 0.0
high = x

ans = (high + low)/2.0

while (abs(ans**2 - x)) >= epsilon:
	guesses += 1
	print('low : ' + str(low) + '   \
		high :  ' + str(high) + '   ans :  ' \
		+ str(ans) + '   guess :  ' + str(guesses))
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0


print(str(ans) + ' is closeish to the root of ' + str(x))


# Trying to extract the above root using an exhaustive test gave thusly:
# Guesses : 499999003
# 4.99999000798 is closeish to the root of 25
# about 500 million guesses
# used a whole core of an i7 for 68 seconds
# raised the CPU temperature by 14C
#
# clearly a better method needs to be found!


# this method resulted in 19 guesses too fast to time.  Sub seconds anyway.
#
# low : 0.0   high :  25   ans :  12.5   guess :  1
# low : 0.0   high :  12.5   ans :  6.25   guess :  2
# low : 0.0   high :  6.25   ans :  3.125   guess :  3
# low : 3.125   high :  6.25   ans :  4.6875   guess :  4
# low : 4.6875   high :  6.25   ans :  5.46875   guess :  5
# low : 4.6875   high :  5.46875   ans :  5.078125   guess :  6
# low : 4.6875   high :  5.078125   ans :  4.8828125   guess :  7
# low : 4.8828125   high :  5.078125   ans :  4.98046875   guess :  8
# low : 4.98046875   high :  5.078125   ans :  5.029296875   guess :  9
# low : 4.98046875   high :  5.029296875   ans :  5.0048828125   guess :  10
# low : 4.98046875   high :  5.0048828125   ans :  4.99267578125   guess :  11
# low : 4.99267578125   high :  5.0048828125   ans :  4.99877929688   guess :  12
# low : 4.99877929688   high :  5.0048828125   ans :  5.00183105469   guess :  13
# low : 4.99877929688   high :  5.00183105469   ans :  5.00030517578   guess :  14
# low : 4.99877929688   high :  5.00030517578   ans :  4.99954223633   guess :  15
# low : 4.99954223633   high :  5.00030517578   ans :  4.99992370605   guess :  16
# low : 4.99992370605   high :  5.00030517578   ans :  5.00011444092   guess :  17
# low : 4.99992370605   high :  5.00011444092   ans :  5.00001907349   guess :  18
# low : 4.99992370605   high :  5.00001907349   ans :  4.99997138977   guess :  19
#
# 4.99999523163 is closeish to the root of 25

