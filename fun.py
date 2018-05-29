import math
def calculateLengthOfTriangle(a,b):
	c = math.sqrt(a**2 + b**2)
	return c



mrgold = calculateLengthOfTriangle(2,4)
print(mrgold)

c1 = calculateLengthOfTriangle(10,5)
print(c1)

for x in range(100):
	for y in range(100):
		z = calculateLengthOfTriangle(x,y)
		print(x,y,z)
