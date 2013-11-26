tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,


#1.Memorize all the escape sequences by putting them on flash cards.
#2.Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
#if your string has quotation marks inside of it and then you would need to escape them
#3.Combine escape sequences and format strings to create a more complex format.
#4.Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. 

#5.Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?

s1 = "so much depends upon {}".format("a red wheel barrow")
print s1

s2=" {1} is better than {0} ".format("emacs", "vim")
print s2

pi = 3.14159
print(" pi = %1.2f " % pi)

##Unit 1 Lesson 3 problem 11
x="hello"
print type(x)
y=True
print type(y)
z=3
print type(z)
a=4.0
print type(a)

