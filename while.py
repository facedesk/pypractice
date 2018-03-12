


secret = 7
number = 0
name = ""

while(number != secret and name.lower() == "iqbal"):
	print("what is your name?")
	name = raw_input(">")
	print("Guess my number between 0 and 10")
	number = int(raw_input(">"))
	if(number < secret):
		print("your number is too low")
	elif(number > secret):
		print("your number is too high")


