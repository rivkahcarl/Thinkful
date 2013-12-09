text = """
Mary had a little lamb,
whose fleece was white as snow.
And everywhere that Mary went,
the lamb was sure to go.
It followed her to school one day
which was against the rule.
It made the children laugh and play,
to see a lamb at school.
And so the teacher turned it out,
but still it lingered near,
And waited patiently about,
till Mary did appear.
"Why does the lamb love Mary so?"
the eager children cry.
"Why, Mary loves the lamb, you know."
 the teacher did reply.
"""

x = text.find("Mary")
print x 
y = text.find("MARY")
print y 
z = text[0:(0+len("Mary"))]
print z

noexist= text.find("Fred")
print noexist
count1 = text.count("Mary")
print count1
count2 = text.count("Fred")
print count2

index1 = text.index("Fred")
print index1
index2 = text.index("Mary")
print index2

##REGEX DIVEINTOPYTHON-Regular_expressions/street_addresses.html
#'ROAD$' - looks for road at the end of the word
# \b means a word boundary must occur here
import re

s = '100 BROAD ROAD'
s2 = re.sub('ROAD$', 'RD.', s)
print s2

s = '100 BROAD ROAD APT. 3'
s2 = re.sub('\bROAD\b', 'RD.', s)
print s2

#7.3 
#^ matches only at beginning of string
#re.search(stringname, 'string that you are looking for')
pattern = '^M{0,3}$'
re.search(pattern,'M')


##Phone Numbers 
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

phonePattern.search('800-555-1212').groups()

#with extension
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
phonePattern.search('800-555-1212-1234').groups()


"""
Summary 
You should now be familiar with the following techniques:

^ matches the beginning of a string.
$ matches the end of a string.
\b matches a word boundary.
\d matches any numeric digit.
\D matches any non-numeric character.
x? matches an optional x character (in other words, it matches an x zero or one times).
x* matches x zero or more times.
x+ matches x one or more times.
x{n,m} matches an x character at least n times, but not more than m times.
(a|b|c) matches either a or b or c.
(x) in general is a remembered group. You can get the value of what matched by using the groups() method of the object returned by re.search.
"""


