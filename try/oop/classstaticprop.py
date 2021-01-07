# from sololearn
# class methods, static methods, properties

# classmethods
# class methods are called by the class and then passed to cls
# Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self parameter of the method.
# Class methods are different - they are called by a class, which is passed to the cls parameter of the method.
# A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod # Class methods are marked with a classmethod decorator
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

# static method
# identical to normal functions of a class
# like classmethods but no additional arguments

class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod # Static methods are marked with a staticmethod decorator
    def add(value1, value2):
        return value1 + value2

        
n1 = int(1)
n2 = int(1)

print(Calculator.add(n1, n2))


# properties
# customizing access to instance attributes
# one common use of a property is to make an attribute read-only

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self): #method pineapple_allowed
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed) # instance attribute pineapple_allowed is called > calls method pineapple_allowed
# works without @property, if typed print(pizza.pineapple_allowed()) > normal function

# properties can also be set by defining setter/getter functions
# the setter function sets the corresponding property's value, the getter gets the value
# @propertyname.setter @propertyname.getter

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


# from realpython

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# Instance methods need a class instance and can access the instance through self.
# Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
# Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
# Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.