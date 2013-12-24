base = raw_input("Please enter number for which you want your base here: ")
base = int(base)
trunk_character = raw_input("Please enter character for your trunk: " )
leaf_character = raw_input("Please enter character for your tree: ")

count = 0
for i in range(1,base, 2):
    star = i
    space = base - i 
    print (space/2) * " " + star * leaf_character + (space/2) * " "

print ((base - 2)/3) * " " + trunk_character * (base/2) + ((base - 2)/3) * " "