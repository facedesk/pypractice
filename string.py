s=raw_input("Please enter a word")

upper_s = s.upper()
print(upper_s)
lower_s = s.lower()
print(lower_s)

combined = upper_s + lower_s

print(combined)

num_s = len(s)
print(num_s)
num_combined = len(combined)

print(num_combined)
halfway = len(s)/2
print(s[halfway])
print("at s[0]")
print(s[0])
last = len(s) - 1
print(s[last])
print(s[-1])

firsthalf = s[:halfway]
lasthalf = s[halfway:len(s)]
print("this should be first/last half")
print(firsthalf)
print(lasthalf)

copy = s[:]

skip = s[1::2]
print(skip)

#value = s[len(s):halfway:-1]
#print(value)
words = s.split()
numberofwords = len(words)
print(words[0:2])
print(words[0:2:-1])
print(words[::-1])

sentence = "\n".join(words)
print(sentence)

newsentence = sentence.replace("\n",":-)")
print(newsentence)






#slice
#start,stop,increment

#concat




'''
print(s.count("l"))



print(s.find("e"))
print(s[:s.find("e")])

replaced = s.replace("great","awesome")
print(replaced)
'''


#s.replace("o","0")





