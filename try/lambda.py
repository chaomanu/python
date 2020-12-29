# lambda functions are anonymous, meaning they can be created on the fly
# they are mostly used when passing a simple expression as an argument to another function
# lambda functions can be assigned to a variable and used like normal functions

# syntax lambda x: expression, arg

n = int(input("input number: "))

#normal func
def doublefunc(x):
    return 2*x
    
print(doublefunc(n))

#lambda func
doublelamb = lambda x: 2*x
print(doublelamb(n))