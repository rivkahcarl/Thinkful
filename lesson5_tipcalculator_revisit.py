##Lesson 5, Tip Calculator Revisited
#meal = float(20)
#tax_value= float(3)
#tip_rate = .15
#tip_value = float(3.45)
#total = meal + tax + tip_value

#calculator= "The base cost of your meal was %s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax, tip_rate, tip_value, total)
#print calculator


meal =float(20)
tax_value= float(3)
meal_with_tax= meal + tax_value
tip=float(.15)
tip_value = tip*meal_with_tax
total = meal_with_tax + tip

text= "The base cost of your meal was $%s \n You need to pay $%s for tax.\n Tipping at a rate of %s, you should leave $%s for the tip.\n The grand total of your meal is $%s" % (meal, tax_value, tip, tip_value, total)
print text
