from functools import reduce

print("prints a list of all numbers from first to second number")
n = int(input("first number "))
m = int(input("second number "))
print("\n")
numberlist = [i for i in range(n,m+1)]
print(numberlist)

#prints a list with numbers from n to m

print("\nadditional tools: \n")

print("sum: ")
numsumvar = reduce(lambda n,m: n+m, numberlist)
print(numsumvar)

# prints the sum of all the numbers in the list

print("even numbers: ")
evennums = [i for i in range(n,m+1) if i % 2 == 0]
print(evennums)

# prints only even numbers

print("odd numbers: ")
evennums = [i for i in range(n,m+1) if i % 2 != 0]
print(evennums)

# prints only odd numbers

### how about a function?
#takes two numbers as input and outputs either all, even or odd numbers in that range (including both numbers)

first =  int(input("first number: "))
second = int(input("second number: ")) + 1

nums = range(first, second)
type = str(input("all, even or odd: "))

def printnumbers(nums, type):
    if type == "all":
        return [num for num in nums]
    if type == "even":
        return [num for num in nums if not num % 2]
    if type == "odd":
        return [num for num in nums if num % 2]

output = printnumbers(nums, type)
print(output)