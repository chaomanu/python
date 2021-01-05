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

class Addition:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.number += other.number
        return self.number

num1 = Addition(int(input("first number: ")))
num2 = Addition(int(input("second number: ")))

add = num1 + num2
print(add)