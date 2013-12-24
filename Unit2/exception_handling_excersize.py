"""
#n = int (raw_input("Please enter a number: "))
while True: 
	try:
		n = raw_input("Please enter an integer: ")
		n = int(n)
		break
	except ValueError:
		print ("No valid integer! Please try again... ")
print "Great, you successfully entered an integer!"
"""
import sys
try:
	f = open('integers.txt')
	s = f.readline()
	i = int(s.strip())
except IOError as (errno, strerror):
	print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
	print "No valid integer in line."
except:
	print "Unexpected error:", sys.exc_info()[0]
	raise