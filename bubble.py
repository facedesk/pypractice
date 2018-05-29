import swap
from visualize import show
import random

#nums = [5,6,1,3,4,10,11,4,2,9,10]
nums = [ random.randint(0,20) for x in range(20)]
#print(nums)
x = 0




while(x < len(nums)-1):
	if(nums[x]>nums[x + 1]):
		nums[x],nums[x+1] = swap.swap(nums[x],nums[x+1])
		x = -1
	show(nums,x,x+1,0.3)
	print(nums)
	x=x+1
print(nums)
