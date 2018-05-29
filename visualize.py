
import time

def show(numbers,x,y=-1,wait=0.3,snumbers=None,count = 0):
	print("\n"*2000)
	print("count=",count)
	print(numbers)
	if(snumbers is not None):
		print(snumbers)
	for index,number in enumerate(numbers):
		display = "+"*number
		if(index==x or index==y):
			display +="<-"
		print(display)
	time.sleep(wait)
	


