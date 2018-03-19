import math
def getDigit():
	i=0
	while(True):
		upper = math.factorial(i) * math.factorial(i) * 2**(i + 1) 
		lower = math.factorial(2*i + 1)
		digit = upper/lower
		print(i,digit)
		i= i +1
getDigit()

