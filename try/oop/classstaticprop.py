# from sololearn
# class methods, static methods, properties

# classmethod
# class methods are called by the class and then passed to cls (normally which is then passed to the self parameter of the method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
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

    @staticmethod
    def add(value1, value2):
        return value1 + value2

        
n1 = int(1)
n2 = int(1)

print(Calculator.add(n1, n2))


# properties
# customizing access to instance attributes

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)