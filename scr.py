def Normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers   


try:
     print Normalize([6, 4, 2])
except ZeroDivisionError, e:
     print 'Invalid maximum element'


	          
