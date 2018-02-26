year = int(input("please enter a year"))
count = 0
while(count < 20):
	year +=1
	if(year % 400):
		print(year + "is a leapyear")
		count +=1
	elif(year % 100):
		pass
	elif(year%4):
		print(year + "is a leapyear")
		count+=1









