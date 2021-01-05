
# inheritance

class superClass:
    def __init__(self, attri, bute):
        self.attri = attri
        self.bute = bute

class subClass(superClass):
    def printing(self):
        print("print something")

first = superClass(1,2) # instance or  object - instance attributes (here 1,2) are unique to each object
second = subClass(3,4)
third = superClass(10,20)

print(first.attri)
print(first.bute)

print(second.attri)
print(second.bute)

print(third.attri, third.bute)

second.printing()
# first.printing() does not work