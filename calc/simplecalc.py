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

while True: 
    try:
        num1 = Calculation(float(input("first number: ")))
        break
    except(ValueError):
        print("not a number")
        continue

ops = ["+", "-", "*", "/", "//", "%", "**"]

type = ""

while True:
    try:
        type = input("Choose operator +, -, *, /, //, %, **; ")
        if type in ops:
            break
        else:
            print("please choose from list")
            continue
    except:
        print("error")
        break

while True:
    try:
        num2 = Calculation(float(input("second number: ")))
        break
    except(ValueError):
        print("not a number")
        continue

print("result: ", end="")

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