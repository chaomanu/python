
# scalable ttt

# s = size

while True:
    try:
        s = int(input("Please specify number for rows/columns "))
        break

    except:
        print("Sorry, please try again.")

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


# 21 22 23 24 25
# 16 17 18 19 20
# 11 12 13 14 15 
# 6  7  8  9  10 
# 1  2  3  4  5  

# row +1   col +s   diag + (s-1)

row1 = list(range(1,s+1))

# range linke seite für reihen
print(1)
print(1+s)
print(1+(s*2))
print(1+(s*3))
print("")

# range rechte seite für reihen (plus 1)
print(s)
print((s*2))
print((s*3))
print((s*4))
print("")

print(list(range(1,(s+1))))
print(list(range((s)+1,(s*2)+1)))
print(list(range((s*2)+1,(s*3)+1)))

"""
1 1+s
1+s 1+s*2
1+s*2 1+s*3

"""

