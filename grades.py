PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREY = '\033[90m'
RESET = '\033[1m'

print(RESET)
grade = float(raw_input("Enter the grade you got on a quiz"))
#todo fill in - and +'s
if(grade >= 90.0):
	print(BLUE+"you got an A")
if(grade >= 80.0 and grade < 90.0):
	print(GREEN+"you got a B")
if(grade >= 70.0 and grade < 80.0):
	print(PURPLE+"you got a C")
if(grade >= 60.0 and grade < 70.0):
	print(YELLOW+"you got a D")
if(grade < 60.0):
	print(RED+"you got an F")
