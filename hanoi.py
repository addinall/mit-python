# Tower of Hanoi - recursive
#
# Mark Addinall - September 2015
# MIT Computer Science - Python

def printMove(fr,to):
	''' 	Recursive Hanoi
		This is non-trivial on an 8 core 7i
		with 16GB of DRAM 
		I let it run until 74,841,558 Iterations until I figured
		the answer will take 18,446,744,073,709,551,615 moves!
		Python is pretty slow at this sorta stuff '''


	printMove.i += 1
	print('move from '+str(fr)+' to '+str(to)+' counter ' + str(printMove.i))

def Towers(n,fr,to,spare):
	if n == 1:
		printMove(fr,to)
	else:
		Towers(n-1,fr,spare,to)
		Towers(1,fr,to,spare)
		Towers(n-1,spare,to,fr)

# test the function(s)

printMove.i = 0
Towers(64, 1,2,3)

