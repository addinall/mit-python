# Mark Addinall - September 2015
# MIT Computer Science - Python
#
# just debugging some pre-loved errors compiled
# by the instructors at MIT


def integerDivision(x, a):
    """
        x: a non-negative integer argument
    a: a positive integer argument

        returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


# print integerDivision(5,3)


def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print("x ==  " + str(x))
    print("a ==  " + str(a))

    if x == a:
	print "x is 0 returning"
        return 0
    elif x < a:
	print("x is less than a, returning x  " + str(x))
        return x
    else:
	print "recursing"
        return rem(x-a, a)

    print("------------------------")

# print rem(2,5)
# print rem(5,5)
# print rem(7,5)

def f(n):
    """
    n: integer, n >= 0.
    """
    print(" n==   " + str(n))
    if n == 0:
        return 1 
    else:
	# print("recursing with return N * f(n -1)" + str(n))
        return n * f(n-1)

print f(4)
print "----------------"
print f(3)
print "----------------"
print f(1)
print "----------------"
print f(0)
print "----------------"


