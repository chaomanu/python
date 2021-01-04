# it's getting harder
# oop # classes

# the syntax for classes looks like this:

class Classname:
    classattribute = "something"                    # may assign an attribute to class that can be accessed from an instances of the class or the class itself

    def __init__ (self, attribute1, attribute2):    # [constructor] takes two arguments and assigns them to the attributes, self must always be the first parameter 
                                                    # __init__ = initializer
        # some code                                 # define the method
        self.attribute1 = attribute1                # access attribute1
        self.attribute2 = attribute2                # access attribute2
        return None                                 # return statement

    # more methods

var = Classname("argument1", "argument2")
print(var.attribute1, var.attribute2)
print(var.classattribute)


print("")

class Simpleclass:
    feuerblumen = 'awesome'
    def __init__ (self, name, mood):                    
        self.name = name
        self.mood = mood
   
    def itis(self):
        print("itishowitis")
    
manu = Simpleclass("manu", "exhausted")
print(manu.name)
print("is")
print(manu.mood)
manu.itis()
print(manu.name + "is" + manu.feuerblumen)
print("")

johnny = Simpleclass("johnny", "chillaf")
print(johnny.name)
print("is")
print(johnny.mood)
johnny.itis()
print(johnny.name + "is" + johnny.feuerblumen)
print("")

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