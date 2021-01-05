"""
__add__ for +
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
"""
# simple calculator
# with classes and magic methods

class Calculation:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.number += other.number
        return self.number

    def __sub__(self,other):
        self.number -= other.number
        return self.number

    def __mul__(self,other):
        self.number *= other.number
        return self.number

    def __truediv__(self,other):
        self.number /= other.number
        return self.number

    def __floordiv__(self,other):
        self.number //= other.number
        return self.number

    def __mod__(self,other):
        self.number %= other.number
        return self.number
    
    def __pow__(self,other):
        self.number **= other.number
        return self.number

num1 = Calculation(int(input("first number: ")))
type = input("Choose operator: + - * / // % ** ")
num2 = Calculation(int(input("second number: ")))


if type == "+":
    add = num1 + num2
    print(add)

elif type == "-":
    sub = num1 - num2
    print(sub)

elif type == "*":
    sub = num1 * num2
    print(sub)

elif type == "/":
    sub = num1 / num2
    print(sub)

elif type == "//":
    sub = num1 // num2
    print(sub)

elif type == "%":
    sub = num1 % num2
    print(sub)

elif type == "**":
    sub = num1 ** num2
    print(sub)