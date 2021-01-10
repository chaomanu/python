
# scalable ttt

# 21 22 23 24 25
# 16 17 18 19 20
# 11 12 13 14 15 
# 6  7  8  9  10 
# 1  2  3  4  5  

# s = size

while True:
    try:
        s = int(input("Please specify number for rows/columns "))
        break

    except:
        print("Sorry, please try again.")

"""

def field(x):
    y = x
    field = x * y
    return x, y, field

fieldsize = (list(field(s)))



r=fieldsize[0] #s
c=fieldsize[1] #s
f=fieldsize[2] #s*s



print("there are " + str(r) + " rows")
print("there are " + str(c) + " columns")
print("there are " + str(f) + " fields")

field = list(range(0,f+1))
print(field)




# row +1   col +s   diag + (s-1)

row1 = list(range(1,s+1))


# range linke seite für reihen
print(1)
print(1+s)
print(1+(s*2))
# ...
print("")

# range rechte seite für reihen (plus 1)
print(s)
print((s*2))
print((s*3))
#...
print("")


print(list(range(1,(s+1))))
print(list(range((s)+1,(s*2)+1)))
print(list(range((s*2)+1,(s*3)+1)))

print("#")

"""

field = [i for i in range(1,s*s+1)]
print(field)

rowlist=[]
def rowprinter():
    x = 0
    while x < s:
        rows = (list(range(1+(x*s),(s+1+(x*s)))))
        yield rows
        x += 1

for r in rowprinter():
    rowlist.append(r)
print(rowlist)


columnlist=[]
def columnprinter():
    x = 0
    while x < s:
        columns = (list(range((1+x), (x + s*s), s)))
        yield columns
        x += 1

for c in columnprinter():
    columnlist.append(c)
print(columnlist)


diagonallist=[]
def diagonalprinter():
    x = 0
    diagonal1 = list(range((1+x), (1+s*s), (s+1)))
    diagonal2 = list(range(s, (s*s), (s-1)))
    diagonallist.append(diagonal1)
    diagonallist.append(diagonal2)

diagonalprinter()
print(diagonallist)


match = ["x" for i in range(s)]
print(match)

x = int(input("number: "))
for n, num in enumerate(field):
    if num == x:
        field[n] = "x"
print(field)

for row in rowlist:
    if x in row:
        for n, num in enumerate(row):
            if num == x:
                row[n] = "x"
print(rowlist)


"""

print("#")

fieldscalable = list(range(1, (s*r)+1))
print(fieldscalable)

print("| ", end="")
for number in fieldscalable:
    print(number,end=" | ")





print("")
print(r)
print(c)
print(f)



1 1+s
1+s 1+s*2
1+s*2 1+s*3

"""

