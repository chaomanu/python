# from sololearn
# classmethod
# class methods are called by the class and then passed to cls

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

        
n1 = int(input("first number: "))
n2 = int(input("second number: "))

print(Calculator.add(n1, n2))