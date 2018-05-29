import random
import min
import swap
import random
from visualize import show


numbers = [random.randint(1,10) for x in range(10)]

def isSorted(data):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            return False
    else:
        return True

def bogosort(data):
    x = 0
    while not isSorted(data):
        random.shuffle(data)
	show(data,0,wait = 0.01,count = x)
        x+=1


bogosort(numbers)
