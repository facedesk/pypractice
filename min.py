def min(nums):
	smallest = nums[0]
	i = 0
	for index,candidate in enumerate(nums):
		if(candidate < smallest):
			smallest = candidate
			i=index
	return smallest,index

def index(nums, number):
	x = 0
	while(x < len(nums)):
		if (number == nums[x]):
			return x
		#print(number,nums[x])
		x+=1
	return -1

#list_of_numbers = [5,1,6,8,3,4,9,-5,-3]
#print(min(list_of_numbers))

