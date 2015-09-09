def gcd(a, b):
	x = min(a, b)
	while (x > 1):
		if ((a % x == 0) and (b % x == 0)):
			break;
		x -= 1
	return x

print gcd(17,12)


