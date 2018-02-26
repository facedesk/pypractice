name = raw_input("Enter your first name")
password = raw_input("Enter your password")

#if omer enters the password dinosaur, say we are logged in
if((name == "omer" and password == "dinosaur") or (name == "pan" and password == "matter")):
	print("you are logged in")

else:
	print("Access denied")


if( not(name == "omer" or name == "tom" or name == "trent")):
	print("thats a cool name")
else:
	print("hmm I don't know that name")


