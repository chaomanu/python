# else statement with for, while, tryexcept

import random

# for loop
# random doubles

n = random.randint(1,10)
for num in range(12):
    n += n
    print(n)
    if n > 9000:
        print("IT'S OVER 9000!!!")
        break
else:
    print("Oh, that's not that bad") # if loop is not broken else is printed

print("")

# while loop
# random 1 or 2

m = random.randint(1,2)
while m != 2:
    print("1")
    break
    
else: print("2")

# tryexcept
# generating a random list and a random number and checking if it's in the list, outputting error or no error if no exception occured

print("")

r = random.randint(1,10)
o = random.randint(1,10)

somelist = range(r)

try:
    for i in somelist:
        print(i)
    print(str(somelist[o]) + " in the list")
except:
    print(str(o) + " not in the list")
    print("error")
else:
    print("no error")