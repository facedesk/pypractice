secret = 7
number = 0

while(number != secret):
	print("Guess my number between 0 and 10")
	number = int(raw_input(">"))
	if(number < secret):
		print("your number is too low")
	elif(number > secret):
		print("your number is too high")


