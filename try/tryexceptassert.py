
# try tries to run a code and if an error (of a certain type) occured the program runs except

m = str(input("Input name: "))

try:
    n = int(input("Input number: "))
except(ValueError):
    print("not a number")

try:
    pwrmsg = "{0}s power level is {1}". format(m,n)
except(NameError):
    print("variable cannot be assigned bc didn't input a number")


try:
    print(pwrmsg)
    if n > int(9000):
        print("IT'S OVER 9000!!!")
except(NameError):
    print("function cannot run bc didn't input a number")


names = "manu", "raffi", "johnny", "karin"
levels = 9001, 1, 2, 3
lvl = {names[0]: levels[0], names[1]:levels[1], names[2]: levels[2], names[3]: levels[3]}

print("power level of {0} is {1}". format(names[0],lvl["manu"]))

try:
    print("{0} and {1} and {2} are kinda on the same lvl". format(names[1], names[2], names[3]))
except: 
    print("error")
try:
    print(names[4])
except(IndexError):
    print("ryan is on another lvl IndexError")
try:
    print(lvl["ryan"])
except(KeyError):
    print("ryan is on another lvl KeyError")