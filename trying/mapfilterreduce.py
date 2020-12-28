# map(), filter(), reduce()

# map() - apply function to each element in an iterable object (lists, tuples, strigns...)
# map(funcion,iterable)

print("\n# map function in use #\n")

nums = [0,1,2,3,4,5,6,7,8,9,10]
numsplusonetimestwo = list(map(lambda x: (x + 1) * 2, nums))
print(numsplusonetimestwo)
#prints even numbers: 1=2, 2=4, 3=6 etc.

stringwhatevs = str("whatever")
stringeachletter = "".join(map(lambda x: str(x) + " *sigh* ", stringwhatevs))
print(stringeachletter)

tuplebinary = ("male", "female")
tupleidentify = "".join(map(lambda x: "I do not identify as " + x + " ", tuplebinary))
print(tupleidentify)

#filter() - filter out object based on a function
# filter(function,iterable)


print("\n# filter function in use #\n")

evennums = [i for i in range(101) if i % 2 == 0]
print(evennums)

def devideten(x):
    if x % 10 == 0:
        return True

tens = list(filter(lambda x: devideten(x), evennums))
print(tens)

# list comprehensions and filter() can achieve the same thing

listtens = [i for i in range(101) if i % 2 == 0 and i % 10 ==0]
print(listtens)

print("\n# reduce function in use #\n")

# can reduce an iterable down to a single cumulative value
# reduce (function, iterable, [initializer]) function needs to take in 2 arguments

from functools import reduce

numlist = [i for i in range(11)]
print(numlist)

numsum = reduce(lambda x,y: x+y, numlist, 0)
print(numsum)

print("let's print the sum of all the integer numbers from first to second number")
n = int(input("first number "))
m = int(input("second number "))

numberlist = [i for i in range(n,m+1)]
print(numberlist)

#prints a list with numbers from n to m

numsumvar = reduce(lambda n,m: n+m, numberlist)
print(numsumvar)

# prints the sum of all the numbers in the list