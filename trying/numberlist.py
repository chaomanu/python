from functools import reduce

n = int(input("first number "))
m = int(input("second number "))

numberlist = [i for i in range(n,m+1)]
print(numberlist)

#prints a list with numbers from n to m

numsumvar = reduce(lambda n,m: n+m, numberlist)
print(numsumvar)

# prints the sum of all the numbers in the list