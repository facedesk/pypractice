story = '''{0}, {0} is the name, was {1} by a 



bus'''
name = raw_input("enter a name")
verb = raw_input("enter a verb")
adjusted = story.format(name, verb)


print(adjusted)
