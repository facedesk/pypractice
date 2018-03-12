socks = "socks"
jeans = "jeans"
laptop = "laptop"
toiletries="toiletries"

luggage = []
item1 = raw_input("what you like to pack?")
luggage.append(item1)
item2 = raw_input("next item to pack?")
luggage.append(item2)


for items in luggage:
	print(items.upper())




grades = [ 
96.0,
100.0,
75.5,
89.5
]

sum = 0

for grade in grades:
	sum = sum + grade
	print(sum)

