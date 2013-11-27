##Lesson 5, Learning Python the Hard Way Excersize 11
print "How old are you?",
age= raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So you're %r old, %r tall and %r heavy" %(age, height, weight)

##1- Pythons raw_input allows to enter input and then save it to be used later on as a string in output
##
print "Here is addition, type one number:"
a= raw_input()
print "type a second number"
b=raw_input()

print "Here are the two added together"
print float(a)+float(b)

##
print "What is your name?"
name= raw_input()
print "Where do you live?"
location=raw_input()
print "What is your goal in life?"
goal=raw_input()

print "My name is %r. I am from %r and my goal in life is %r" %(name, location, goal)