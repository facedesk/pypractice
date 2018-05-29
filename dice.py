#Players have resources avaiable to them : food & water starting at 20
#Players Rolls that are between 0-2 mean the player is eating decrease by 2 food & water, 2-4 means gather food increase by 2, 4-6 means gather water increase by 2
#Players Roll two dice
#The player to last the longest wins
#When the two die match, the player may choose to attempt to steal resources from the other player
#The player may choose how much to attempt to steal, 1-6. The player must roll better than the amount they steal to take it. 
#When you lose, you must give that amount to the other player

import random

def roll(player,beginning,end):
	print(player, " is about to roll")
	raw_input("Press enter to roll")
	r1 = random.randint(beginning,end)
	r2 = random.randint(beginning,end)
	return r1,r2

def adjustSupply(roll,player):
	if(roll > 4):
		player["water"] +=2
	elif(roll > 2):
		player["food"] +=2
	elif(roll > 0):
		player["water"] -=2
		player["food"] -=2
def checkStock(player):# stubbed
	return True

def takeTurn(player,players):
	r1,r2 = roll(player["name"],1,6)
	adjustSupply(r1,player)
	adjustSupply(r2,player)
	if(checkStock(player) == False):
		return player
	if(r1==r2):
		trySteal(player,players)
	return ""
def steal(player1,player2,amount):
	player1["water"] += amount
	player1["food"] += amount
	player2["water"] -= amount
	player2["water"] -= amount
def trySteal(player,players):
	print("type the number of the player you want to steal from")
	for i,p in enumerate(players):
		if(p == player):
			continue
		print(str(i) + ")    \n", p) 
	victim = players[int(raw_input(">"))]
	
	print(victim)
	supply = raw_input("how much supply of both food/water do you want to attempt to steal? 1-6")
	supply = int(supply)
	r1,r2 = roll(player,1,6)
	print("you rolled....",r1, "and need to meet or beat",supply)
	if(r1 >= supply):
		steal(player,victim,supply)
	else:
		steal(victim,player,supply)

def game(players):
	GameRunning = True
	lost = ""
	while(GameRunning):
		for player in players:
			print(player)
			print(" its your turn!")
			lost = takeTurn(player,players)
			if(lost != ""):
				return lost

nump = 0
while(nump < 2):
	print("how many players would you like?")
	nump = int(raw_input(">"))
players = []
for x in range(nump):
	name = raw_input("enter players name")
	players.append({"name":name,"food":20,"water":20})




game(players)

