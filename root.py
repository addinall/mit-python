def root(x, power, epsilon):
	"""	x and epsilon - int or float
		power an it
		epsilon > 0
		power >= 1

		returns a float if valid
		returns None if invalid		"""

	if X < 0 and power % 2 == 0:
		return None
	# we can't find the even powered root of a negative number

	low = min(-1, x)
	high = max(1, x)
	ans = (high + low) / 2.0
	while abs(ans**power - x) > epsilon:
		if ans**power < x:
			low = ans
		else:
			high = ans
		ans = (high + low) / 2.0
	return ans


