# balance2.py
#
# A little program that calculates the minimum fixed monthly payment 
# needed in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does 
# not change each month, but instead is a constant amount that will be 
# paid each month.
#
# Mark Addinall.  MIT CompSci 6.00/1X
#
# Sep 2015

balance 		= 3926 
annualInterestRate 	= 0.2

monthly_interest_rate 	= annualInterestRate / 12

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

payment = 0
finished = False
debt = balance

while not finished:
	# we could pick a smarter start point than this,
	# however, this seems to be in the spirit of the
	# Lab instructions.

	payment += 10
	debt = run_year(payment, balance)
	finished = (debt <= 0)

print('Lowest Payment: ' + str(payment))


