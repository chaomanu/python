
# prints exponential numbers from 1 to m

print("first number is 1")
m = int(input("second number "))

numlist = [i for i in range(m+1)]
print(numlist)

x=0
y=1

for i in numlist:
    print(x, end=", ")
    x = y
    y = x+y

    