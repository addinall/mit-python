# balance.py
#
# A little program that computes a decreasing balance of a compound
# debt over a period of 12 months.  Iterative calculation.
#
# Mark Addinall.  MIT CompSci 6.00/1X
#
# Sep 2015

balance 		= 4842
annualInterestRate 	= 0.2
monthlyPaymentRate 	= 0.04

total_paid_year 	= 0

monthly_interest_rate 	= annualInterestRate / 12
minimum_monthly_payment = 0

for month in range(12): 
	print('Month: ' + str(month + 1))
	minimum_monthly_payment = monthlyPaymentRate * balance
	print('Minimum monthly payment: %.2f' % minimum_monthly_payment)
	total_paid_year += minimum_monthly_payment
	balance -= minimum_monthly_payment
	interest = balance * monthly_interest_rate
	# print('Interest : %.2f' % interest)
	balance += interest
	print('Remaining balance: %.2f' % balance)
	

print('Total paid: %.2f' % total_paid_year)
print('Remaining balance: %.2f' % balance)
