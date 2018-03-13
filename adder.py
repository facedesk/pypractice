def add(a,b):
	c = a+b
	return c
def multiply(a,b):
	c = 0
	for x in range(a):
		c = add(c,b)
	return c
def pow(a,b):
	c = 1
	for x in range(b):
		print(c,"pow")
		c = multiply(a,c)
	return c
y = pow(1,2)
z = pow(3,4)
x2= 1 ** 2
x3= 3 ** 4 


print(y,z)
print(x2,x3)
