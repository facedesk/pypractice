coins = [
[0.25,0],
[0.1,0],
[0.05,0],
[0.01,0]
]
def sum(coins):
	sum = 0
	for coin in coins:
		sum += coin[0]*coin[1]
	return sum
def generate(coins):
	for c in coins:
		print(c)
		if(sum(coins)+ c[0]!=1):
			c[1]+=1
#			return generate(coins) 
		else:
			return coins
print(generate(coins))
