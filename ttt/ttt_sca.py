import time
import random

# input for fieldsize
while True:
    try:
        s = int(input("choose size (number of fields per row/column): "))
        if s <= 1:
            print("please choose a higher number")
            continue
        break
    except(ValueError):
        print("not a number")

# list for field
field = [i for i in range(1,s*s+1)]
print(field)

# rows, columns and diagonals for winconditions

rowlist=[]
def rowprinter():
    """ creates a list with all rows"""
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
    """creates a list with all columns"""
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
    """creates a list with all diagonals"""
    x = 0
    diagonal1 = list(range((1+x), (1+s*s), (s+1)))
    diagonal2 = list(range(s, (s*s), (s-1)))
    diagonallist.append(diagonal1)
    diagonallist.append(diagonal2)

diagonalprinter()
print(diagonallist)

# match for wincondition
match = ["x" for i in range(s)]
print(match)

def userinput(x):
    for n, num in enumerate(field):
        if num == x:
            field[n] = "x"
    
    for row in rowlist:
        if x in row:
            for n, num in enumerate(row):
                if num == x:
                    row[n] = "x"
    return field, rowlist


while True:
    try:
        x = int(input("number: "))
        x in field
        userinput(x)
        print(field)
        print(rowlist)
        if all(type(i) is str for i in field):
            print("Game over")
            break

    except(ValueError):
        print("not a number!")
        



"""

def printmatrix():
    print("", *rowlist[2],"", sep = "|")
    print("", *rowlist[1],"", sep = "|")
    print("", *rowlist[0],"", sep = "|")

def matrixdeko(printmatrix):
    def wrap():
        print("\n")
        printmatrix()
        print("\n")
    return wrap

dekomatrix = matrixdeko(printmatrix)

### inputs

def userinput():
    try:
        x=int(input("Please input 1-9: "))
        if x in list:    
            print("you draw x at " + str(x) + " " + positions[x])
            list[x] = "x"
            list.append("c")
        else:
            print("that...was not a valid input (not available)")
            
    except ValueError:
        print("that...was not a valid input (not a number)")

def botinput():
    o = random.randint(1,9)
    while o not in list and len(list) < 19:
        o = random.randint(1,9)
    if o in list:
        print("randobot draws o at " + str(o) + " " + positions[o])
        list[o] = "o"
        list.append("c")      


### messages

winboommsg = "BOOM!\ntetris for jeff\n"
winprettymsg = "omg so pretty \n"
winmsg = "You won! Suck it, randobot!"
lossmsg = "Oh no! You got owned by randobot!"
drawmsg = "No winner! (lame)"


### gameresults

def winpretty():

    row2 = list[4:7]
    col2 = list[2:9:3]

    trix = ["x", "x", "x"] 

    if (row2 == trix and col2 == trix):
        return True

def winboom():
    "function that determines when easteregg win is triggered"

    row1 = list[1:4]
    row2 = list[4:7]
    row3 = list[7:10]
    col1 = list[1:8:3]
    col2 = list[2:9:3]
    col3 = list[3:10:3]
    dia1 = list[1:10:4]
    dia2 = list[3:8:2]

    trix = ["x", "x", "x"]
    
    if (row1 == trix and col1 == trix) or (row2 == trix and col1 == trix) or (row3 == trix and col1 == trix):       
        return True
    elif (row1 == trix and col2 == trix) or (row2 == trix and col2 == trix) or (row3 == trix and col2 == trix):        
        return True
    elif (row1 == trix and col3 == trix) or (row2 == trix and col3 == trix) or (row3 == trix and col3 == trix):     
        return True
    elif (dia1 == trix and row1 == trix) or (dia1 == trix and row2 == trix) or (dia1 == trix and row3 == trix):  
        return True
    elif (dia2 == trix and row1 == trix) or (dia2 == trix and row2 == trix) or (dia2 == trix and row3 == trix):
        return True   
    elif (dia1 == trix and col1 == trix) or (dia1 == trix and col2 == trix) or (dia1 == trix and col3 == trix):
        return True
    elif (dia2 == trix and col1 == trix) or (dia2 == trix and col2 == trix) or (dia2 == trix and col3 == trix):
        return True

def wincondition():
        
    row1 = list[1:4]
    row2 = list[4:7]
    row3 = list[7:10]
    col1 = list[1:8:3]
    col2 = list[2:9:3]
    col3 = list[3:10:3]
    dia1 = list[1:10:4]
    dia2 = list[3:8:2]

    trix = ["x", "x", "x"]

    if row1 == trix or row2 == trix or row3 == trix:
        return True
    elif col1 == trix or col2 == trix or col3 == trix:
        return True
    elif dia1 == trix or dia2 == trix:
        return True
    
def losscondition():

    row1 = list[1:4]
    row2 = list[4:7]
    row3 = list[7:10]
    col1 = list[1:8:3]
    col2 = list[2:9:3]
    col3 = list[3:10:3]
    dia1 = list[1:10:4]
    dia2 = list[3:8:2]

    trio = ["o", "o", "o"]

    if row1 == trio or row2 == trio or row3 == trio:
        return True
    elif col1 == trio or col2 == trio or col3 == trio:
        return True
    elif dia1 == trio or dia2 == trio:
        return True



yesses = ["Yes", "yes", "Y", "y", "Ya", "ya", "Yass", "yass", "1"]
noes = ["No", "no", "N", "n", "Nope", "nope", "Nah", "nah", "2"]
startwords = yesses + noes


while True:
    starter = input("Do you want to go first? Yes or No? ")
    if starter not in startwords:
        print("You failed to answer the yes/no question")
    else:
        break
# determines who goes first - player or bot

print("Here we go!")

### game

def firstmove():
    if starter in noes:
        botinput()

while True:

    firstmove()

    dekomatrix()

    for number in list:   
        
        userinput()

        if winboom() == True:
            dekomatrix()
            print(winboommsg)
            if winpretty() == True:
                print(winprettymsg)
            print(winmsg)
            break

        elif wincondition() == True:
            dekomatrix()
            print(winmsg)
            break   
     
        botinput()

        dekomatrix()

        if losscondition() == True:
            if winpretty() == True:
                print(winprettymsg)
            print(lossmsg)
            break  


        if len(list) > 18:
            print(drawmsg)
            break



    print("Game over")

    yesses = ["Yes", "yes", "Y", "y", "Ya", "ya", "Yass", "yass", "1"]
    noes = ["No", "no", "N", "n", "Nope", "nope", "Nah", "nah", "2"]
    startwords = yesses + noes

    while True:
        playagain = str(input("Do you want to play again? "))
        if playagain not in startwords:
            print("You failed to answer the yes/no question")
        elif playagain in startwords:
            break

    if playagain in yesses:
            field = ["new field"]
            continue
    elif playagain in noes:
            print("OK, bye-ee!")
            time.sleep(5)
            break
"""