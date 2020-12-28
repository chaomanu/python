from functools import reduce

print("let's print the sum of all numbers from first to second number")
n = int(input("first number "))
m = int(input("second number "))

numberlist = [i for i in range(n,m+1)]
print(numberlist)

#prints a list with numbers from n to m

numsumvar = reduce(lambda n,m: n+m, numberlist)
print("sum is ", end = "")
print(numsumvar)

# prints the sum of all the numbers in the list