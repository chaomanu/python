# it's getting harder
# let's test some oop with classes

"""
the syntax for classes looks like this:

class Classname:
    (class attribute = something                        # may assign an attribute to class that can be accessed from instances of the class or the class itself)

    def __init__ (self, attribute1, attribute2)         # [constructor] takes two arguments and assigns them to the attributes, self must always be the first parameter 
        some code                                       # define the method
        self.attribute1                                 # access attribute1
        self.attribute2                                 # access attribute2
        return if necessary                             # return statement

    more methods

variable = Classname(argument1, argument2)
print(variable.attribute)
etc.
"""

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

first = superClass(1,2)
second = subClass(3,4)

print(first.attri)
print(first.bute)
print(second.attri)
print(second.bute)

second.printing()
# first.printing() does not work