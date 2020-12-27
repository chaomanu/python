#trying generators
while True:
    try:
        y = int(input("print a list with numbers up until "))
        break
    except:
        print("type a number")

list = []

def gen(y):
    x = 0
    while x < y:
        x += 1
        yield x

for x in gen(y):
    list.append(x)

print(list)