from copy import deepcopy

coins = [
[0.25,0],
[0.1,0],
[0.05,0],
[0.01,0]]

TargetToMiss=1
NetValue = 0

def CanAddCoin(coins,coin,index,TargetToMiss):
	sum = coin
	if(index > len(coins)-1): #if there are no more coins left to process
		return True
	elif(coins[index][1]==0): #if all coins of this category have been added up
		index+=1
	else:
		coins[index][1]-=1 # we have tried this value so check if its missing one
	for c in coins:
		sum = sum + c[0] * c[1]
		print(index)
	return  sum != TargetToMiss and CanAddCoin(coins,coin,index,TargetToMiss) 


for index in range(len(coins)):
	while(CanAddCoin(deepcopy(coins),coins[index][0],0,TargetToMiss)):
		coins[index][1] =coins[index][1] + 1
		print(coins)
print("final answer is", coins)	



