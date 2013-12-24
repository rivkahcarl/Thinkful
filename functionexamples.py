"""
a_var = 10
b_var = 15
e_var = 25

def a_func(a_var):
	print "in a_func a_var = ", a_var
	b_var = 100 + a_var
	d_var = 2 * a_var
	print "in a_func b_var = ", b_var
	print "in a_func d_var = ", d_var
	print "in a_func e_var = ", e_var
	return b_var + 10

c_var = a_func(b_var)

print "a_var = ", a_var
print "b_var = ", b_var
print "c_var = ", c_var
print "d_var = ", d_var
"""

"""
def print_options():
	print "Options:"
	print " 'p' print options"
	print " 'c' convert from celsius"
	print " 'f' convert from fahrenheit"
	print " 'q' quit the program"

def celsius_to_fahrenheit(c_temp):
	return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
	return (f_temp - 32.0) * 5.0 / 9.0

choice = "p"
while choice != "q":
	if choice == "c":
		temp = input("Celsius temperature: ")
		print "Fahrenheit:", celsius_to_fahrenheit(temp)
	elif choice == "f":
		temp = input("Fahrenheit temperature: ")
		print "Celsius:", fahrenheit_to_celsius(temp)
	elif choice != "q":
		print_options()
	choice = raw_input("option: ")
"""
#area of rectangle example
"""
print 
def hello():
	print 'Hello!'

def area(width, height):
	return width * height

def print_welcome(name):
	print 'Welcome,', name

name = raw_input('Your Name: ')
hello(),
print_welcome(name)
print 
print 'to find the area of a rectangle,'
print 'enter the width and height below.'
print
w = input('Width: ')
while w <= 0:
	print 'Must be a positive number'
	w = input ('Width: ')

h = input('Height: ')
while h <= 0:
	print 'Must be a positive number'
	h = input('Height: ')

print 'Width =', w, 'Height =', h, 'so Area =', area(w, h)
"""

#area of square
print 
def hello():
	print 'Hello!'

def area(width, height):
	return width * height

def print_welcome(name):
	print 'Welcome,', name

name = raw_input('Your Name: ')
hello(),
print_welcome(name)
print 
print 'to find the area of a rectangle,'
print 'enter the width and height below.'
print
w = input('Width: ')
while w <= 0:
	print 'Must be a positive number'
	w = input ('Width: ')

h = input('Height: ')
while h <= 0:
	print 'Must be a positive number'
	h = input('Height: ')

print 'Width =', w, 'Height =', h, 'so Area =', area(w, h)
"""
