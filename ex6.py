#defines x as a string inserting the number 10 in the place of the %d
x = "There are %d types of people." % 10
#assigns the string binary to the variable binary
binary = "binary"
#assigns the string don't to the variable do_not
do_not = "don't"
#assigns y to be the sentance where the value of the binary variable is put in the first string spot and the value of the do_not varialbe is put in the last 
y = "Those who know %s and those who %s." % (binary, do_not)
#prints the x and y statements
print x
print y

#prints the statement while inserting the x in the %r spot. similarly with y
print "I said: %r." % x
print "I also said: '%s'." % y

#assigns the variable hilarious to be false and joke_evaluation to be the sentence
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#prints the sentence of joke_evaluation with the value of the hilarious variable 
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#concatenates together the two string sentances
print w + e