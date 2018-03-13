PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREY = '\033[90m'
RESET = '\033[0m'

def printred(message):
	print(RED + message + RESET)
def printgreen(message):
	print(GREEN + message + RESET)
def printyellow(message):
	print()
	print(YELLOW + message + RESET)
	print()
def printrgy(message):
	letterIndex = 0
	newmessage = ""
	while(letterIndex < len(message)):
		if(letterIndex % 3 == 0):
			newmessage += RED
		elif(letterIndex % 3 == 1):
			newmessage += GREEN
		elif(letterIndex % 3 == 2):
			newmessage += YELLOW
		newmessage = newmessage + message[letterIndex]
		letterIndex +=1
	print(newmessage + RESET)
printrgy("enter rainbow road, you will never come out in first place")
for x in range(10):
	printyellow("hello")
	printyellow("goodbye")








printred("Hello")
printgreen("Merry")
printred("Christmas!!!")
printred("wait, how does this work?")








