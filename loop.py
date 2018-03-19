frame = 0
totalScore = 0
while(frame < 10):
	print("enter the ",frame)
	bowl = raw_input("what did you bowl?")
	totalScore += int(bowl)
	frame +=1
print(totalScore)
