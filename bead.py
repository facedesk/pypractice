nums = [2,4,1,3,3]
sorted = []

done = False
while(not done):
	print("iteration")
	zeros = True
	print(sorted)
	score = 0
	for x,i in enumerate(nums):
		if(i ==0):
			pass
		else:
			score +=1
			zeros = False
			nums[x]-=1
			
	sorted.append(score)
	done = zeros
print(sorted)
