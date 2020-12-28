
numlist = [i for i in range(11)]
print(numlist)

x=0
y=1

for i in numlist:
    print(x)
    x = y
    y = x+y

    