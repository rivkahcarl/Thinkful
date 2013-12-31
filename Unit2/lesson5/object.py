class User(object):
    def __init__(self, name):
        self.name= name
    def introduce(self):
        print "My name is ", self.name

def change(string, object):
    string = "new name"
    object.name = "another new name"

fred = User("fred")
bill = "bill"

fred.introduce()
print bill

change(bill, fred)

fred.introduce()
print bill