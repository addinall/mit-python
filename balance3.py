# balance3.py
#
# Sameish deal as balance2.py. rxcept this time we will use some smarts
# (a bisection search) to get the payment amount rather than brute
# forcing the result as a multiple of ten bucks.
#
# Write a program that uses these bounds and bisection search (for 
# more info check out the Wikipedia page on bisection search) to find 
# the smallest monthly payment to the cent (no more multiples of $10) 
# such that we can pay off the debt within a year. 
#
#
# Mark Addinall.  MIT CompSci 6.00/1X
#
# Sep 2015

balance 		= 999999 
annualInterestRate 	= 0.18

monthly_interest_rate 	= annualInterestRate / 12.0

def run_year(fixed_payment, arg_balance):
	""" for a given outstanding balance, calculate a payment
	    run for 12 months, that is 12 X fixed payments,
	    calculating accrued interest, and return the result
	    of the run """

	for month in range(12): 
		arg_balance -=  fixed_payment
		interest = arg_balance * monthly_interest_rate
		arg_balance += interest
	return arg_balance

finished 		= False

# epsilon is our 'close enough' value
epsilon			= 0.01

#first guess is the debt div 12 (sans compound interest)
bottom 			= balance / 12.0

# top has maximum interest levied for total period
top			= (balance * (1 + monthly_interest_rate)**12)/12.0

while not finished:
	# make a binary chop
	payment = (bottom + top) / 2.0
	# calculate a year run at these monthly payments
	debt = run_year(payment, balance)
	# are we within a fraction of one cent?  Good enough.
	finished = (abs(debt) < epsilon)
	# do the binary high/low re-scale and continue
	if debt < 0:
		top = payment
	elif debt > 0:
		bottom = payment

print('Lowest Payment: ' + str(round(payment,2)))


