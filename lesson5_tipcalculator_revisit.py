##Lesson 5, Tip Calculator Revisited
#done alone before directions
#meal = float(20)
#tax_value= float(3)
#tip_rate = .15
#tip_value = float(3.45)
#total = meal + tax + tip_value

#calculator= "The base cost of your meal was %s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax, tip_rate, tip_value, total)
#print calculator

#after first part of directions
#meal =float(20)
#tax_value= float(3)
#meal_with_tax= meal + tax_value
#tip=float(.15)
#tip_value = tip*meal_with_tax
#total = meal_with_tax + tip

#text= "The base cost of your meal was $%s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax_value, tip, tip_value, total)
#print text

##raw input method

#meal = raw_input("The base of my meal is: ")
#tax_percent = raw_input("What is the percentage of tax at the restaurant? Please enter in decimal format: ")
#tax= float(tax_percent)* float(meal)
#pre_tip = float(meal) + float(tax)
#tip = raw_input("Please enter the percent of tip you would like to add? (in decimal format): ")
#tip_tot= float(tip)*pre_tip 
#total=  tip_tot + pre_tip

#text = "The base cost of your meal was $%s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax, tip, tip_tot, total)
#print text

##user supplied variables with sys.argv
##arguments go directly in command line

import sys

#meal=sys.argv[1]
#tax_percent= sys.argv[2]
#tip = sys.argv[3]
#tax= float(tax_percent)* float(meal)
#pre_tip = float(meal) + float(tax)
#tip_tot= float(tip)*pre_tip 
#total=  tip_tot + pre_tip

#text = "The base cost of your meal was $%s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax, tip, tip_tot, total)
#print text

##Using OptionParser

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal_arg", help="meal cost", type="float")
parser.add_option("-t", "--tax_rate", dest="tax_rate_arg", help="tax rate for meal", type="float")
parser.add_option("-r", "--tip_rate", dest="tip_rate_arg", help="tip rate for meal", type="float")

(options, args) = parser.parse_args()

meal=options.meal_arg
print meal
tax_percent= options.tax_rate_arg
print tax_percent
tip = options.tip_rate_arg
print tip
tax= float(tax_percent)* float(meal)

pre_tip = float(meal) + float(tax)
tip_tot= float(tip)*pre_tip 
total=  tip_tot + pre_tip

text = "The base cost of your meal was $%s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax, tip, tip_tot, total)
print text



