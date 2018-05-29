import min
import random
from visualize import show
numbers = [random.randint(1,10) for x in range(10)]
print(numbers)
print("\n\n\n")
numberscopy = numbers
ordered = []
while(len(numbers) > 0):
	smallest,index = min.min(numberscopy)
	show(numberscopy,index,snumbers=ordered,wait=1)
	print(numberscopy)
	print(ordered)
	ordered.append(smallest)
	numberscopy.remove(smallest)
	
print(ordered)

