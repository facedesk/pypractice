#todo, change to random number
import random

answer = random.randint(0,5)

guess = int(raw_input("Enter a number, 0-5:"))

print(answer,guess)

if(guess > answer):
	print("Your number is too high")
	guess = int(raw_input("Enter a number, 0-5:")

elif(guess < answer):
	print("Your number is too low")

elif(guess == answer):
	print("Yes, you guessed my number")

