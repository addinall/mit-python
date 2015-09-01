x = 25
epsilon = 0.01
step = epsilon**2
guesses = 0
ans = 0.0

while (abs(ans**2 - x)) >= epsilon and ans <= x:
	ans += step
	guesses += 1
print('Guesses : ' + str(guesses))
if abs(ans**2 - x) >= epsilon:
	print('Failed on root of ' + str(x))
else:
	print(str(ans) + ' is closeish to the root of ' + str(x))

# the above code takes about 50,000 guesses to return
# 4.999 as a valid result

x = 25
epsilon = 0.0001
step = epsilon**2
guesses = 0
ans = 0.0

while (abs(ans**2 - x)) >= epsilon and ans <= x:
	ans += step
	guesses += 1
print('Guesses : ' + str(guesses))
if abs(ans**2 - x) >= epsilon:
	print('Failed on root of ' + str(x))
else:
	print(str(ans) + ' is closeish to the root of ' + str(x))

# Guesses : 499999003
# 4.99999000798 is closeish to the root of 25
# about 500 million guesses
# used a whole core of an i7 for 68 seconds
# raised the CPU temperature by 14C
#
# clearly a better method needs to be found!


