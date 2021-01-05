# it's getting harder
# object oriented programming

"""
paradigms:
imperative - statements, loops, functions as subroutines
functional - pure functions, higher-order functions, recursions 
oop - objects

"""
# syntax for classes:

class Classname: 
    classattribute = "classattribute"                # assigns attribute to class that can be accessed from an instances of the class or the class itself
                                                    
    def __init__ (self, attribute1, attribute2):    # __init__ method - creates an instance (object) of the class (using Classname as a function)
                                                    #  takes (itc) two arguments and assigns them to the attribute(s), self must always be the first parameter  
                                                    # attributes are accessed with self.attribute           
        self.attribute1 = attribute1                # sets initial value of attribute1 
        self.attribute2 = attribute2                # sets initial value of attribute2
   
    def anothermethod (self):                       # other methods (besides the __init__ method) can be added (all must have self as first parameter)
        print("anothermethod")                      # can be accessed the same way as attributes with self.anothermethod() > () because it's a function not an attribute

    def usingclassattribute(self):                  # class accessing classattribute
        return self.classattribute

var = Classname("argument1", "argument2")           # uses the class (blueprint) to define an object and bind it to a variable
var2 = Classname("argument3", "argument4")          # the same class (blueprint) can create different objects with different values

# print
print(var.attribute1)
print(var.attribute2)
print(var2.attribute1)
print(var2.attribute2)

print(var.classattribute)                           # instance of the class accessing classattribute
var.anothermethod()                                 # instance of the class accessing method anothermethod
print(var.usingclassattribute())                    # instance of the class accessing method usingclassattribute

# facts:
# objects are created using classes
# classes contain methods (which are functions) 
# the class describes what the object will be, but is separate from the object itself (like a blueprint)
# __init__ method = initializer = constructor > creates instance(object) of the class
# instance = object
# instances of a class have attributes, which are pieces of data associated with them
# in an __init__ method, self.attribute can be used to set the initial value of an instance's attributes
# within a method definition, self refers to the instance calling the method

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