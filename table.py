'''
Write a python function called make_table that takes in an integer
and displays a multiplication table of that integers size
e.g.

make_table(4)

   [1][2][3][4]
[1] 1  2  3  4
[2] 2  4  6  8
[3] 3  6  9  12
[4] 4  8  12 16



'''

def make_table(number):
	title = '   '
	for left_operand in range(1,number+1):
		title = title + '['+str(left_operand)+']'
	print(title)
	for right_operand in range(1,number+1):
		row = '['+str(right_operand)+']'
		for left_operand in range(1,number+1):
			multiplied = str(left_operand * right_operand)
			if(len(multiplied) >2):
				row = row + multiplied
			elif(len(multiplied) > 1):
				row = row + multiplied + ' '
			else:
				row = row + ' '+multiplied+' '
		print(row)
x = 9
make_table(x)



