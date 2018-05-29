#import min
import swap
import random
from visualize import show


numbers = [random.randint(1,10) for x in range(10)]

def selectionsort(numbers):
	x = 0
	for i in range(len(numbers)):
		smallest = min(numbers[i:])
		sm_index = numbers[i:].index(smallest)
		show(numbers,i,i+sm_index,wait=1)
		numbers[i+sm_index],numbers[i] = swap.swap(numbers[i+sm_index],numbers[i])
	print(numbers)


selectionsort(numbers)

