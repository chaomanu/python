# it's getting harder
# object oriented programming

"""
paradigms:
imperative - statements, loops, functions as subroutines
functional - pure functions, higher-order functions, recursions 
oop - objects

"""

# the class describes what the object will be, but is separate from the object itself (like a blueprint)
# syntax for classes:

class Classname: 
    classattribute = "something"                    # may assign an attribute to class that can be accessed from an instances of the class or the class itself
                                                    #classes contain methods (functions)
    def __init__ (self, attribute1, attribute2):    # [constructor] takes (itc) two arguments and assigns them to the attribute(s), self must always be the first parameter 
                                                    # __init__ = initializer
        self.attribute1 = attribute1                # sets initial value of attribute1 
        self.attribute2 = attribute2                # sets initial value of attribute2

    # more methods if needed (must all have self as first parameter)

#CLASS - blueprint ↑
# OBJECT - uses blueprint ↓

var = Classname("argument1", "argument2")           # defines an object  
var2 = Classname("argument3", "argument4")          # defines another object

# print
print(var.attribute1, var.attribute2)
print(var.classattribute)

print("")

class Simpleclass:
    feuerblumen = 'awesome'
    def __init__ (self, name, mood):                    
        self.name = name
        self.mood = mood
   
    def itis(self):
        print("itishowitis, ", end="")
        print(self.name)
    
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