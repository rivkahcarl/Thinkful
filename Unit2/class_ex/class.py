class Store:
    inventory = {}
    name = None
    employees = None

    def __init__(self, name, inventory, employees=None):
        self.name = name
        self.inventory = inventory
        self.employees = employees

    def countinv(itemname, itemvalue=1):
        if itemname in self.inventory:
            if self.inventory[itemname] >= itemvalue:
                return True
        return False

    def changeinv(itemname, itemvalue=1):
        if itemvalue < 0:
            if not countinv(itemname, itemvalue): 
                return False
        self.inventory[itemname] = self.inventory.get(itemname,0) + itemvalue
        return True

class Cart:
    items = {}
    store = None
    customername = None

    def __init__(self, customername, store):
        self.customername = customername
        self.store = store

    def addtocart(itemname, itemvalue):
        

## Add to cart and remove from cart function, 
## display store inventory 



mystore = Store("Rivkah's Store", {'fruits':5, 'vegetables':10}, employees = 25)
mystore.changeinv('fruits', 2)


mysecondstore = Store("Rivkah's Store 2", {'fruits':50, 'vegetables':100}, employees = 35)
mysecondstore.changeinv('fruits', 23)