import time
import random

# input for fieldsize
while True:
    try:
        s = int(input("choose size (number of fields per row/column): "))
        if s <= 1:
            print("please choose a higher number")
            continue
        if s > 10:
            print("that's a bit excessive, don't you think?")
            continue
        break
    except(ValueError):
        print("not a number")

# list for field
field = [i for i in range(1,s*s+1)]

# rows, columns and diagonals for winconditions
rowlist=[]
def row():
    """ creates a list with all rows"""
    x = 0
    while x < s:
        rows = (list(range(1+(x*s),(s+1+(x*s)))))
        yield rows
        x += 1

for r in row():
    rowlist.append(r)

collist=[]
def col():
    """creates a list with all columns"""
    x = 0
    while x < s:
        columns = (list(range((1+x), (x + s*s), s)))
        yield columns
        x += 1

for c in col():
    collist.append(c)

dialist=[]
def dia():
    """creates a list with all diagonals"""
    x = 0
    diagonal1 = list(range((1+x), (1+s*s), (s+1)))
    diagonal2 = list(range(s, (s*s), (s-1)))
    dialist.append(diagonal1)
    dialist.append(diagonal2)

dia()

# match for wincondition and losscondition
match = [" x" for i in range(s)]
fail = [" o" for i in range(s)]

# userinput
def userinput(x):
    """asks userinput until valid number and adds " x" to the field"""
    for n, num in enumerate(field):
        if num == x:
            field[n] = " x"
    
    for row in rowlist:
        if x in row:
            for n, num in enumerate(row):
                if num == x:
                    row[n] = " x"

    for col in collist:
        if x in col:
            for n, num in enumerate(col):
                if num == x:
                    col[n] = " x"

    for dia in dialist:
        if x in dia:
            for n, num in enumerate(dia):
                if num == x:
                    dia[n] = " x"

    return field, rowlist, collist, dialist

# botinput
def botinput():
    """generates a random number in range and draws " o" on the field"""
    o = random.randint(1,s*s)
    while o not in field:
        o = random.randint(1,s*s)
    if o in field:
        for n, num in enumerate(field):
            if num == o:
                field[n] = " o"
        
        for row in rowlist:
            if o in row:
                for n, num in enumerate(row):
                    if num == o:
                        row[n] = " o"

        for col in collist:
            if o in col:
                for n, num in enumerate(col):
                    if num == o:
                        col[n] = " o"

        for dia in dialist:
            if o in dia:
                for n, num in enumerate(dia):
                    if num == o:
                        dia[n] = " o"
        return field, rowlist, collist, dialist

# print field
revfield = rowlist.reverse()
def printfield():
    """ prints the field """
    for row in rowlist:
        revfield
        print("|", end="")
        for nums in row:
            if nums in range(1,10):
                print(" ", end="")
            if nums == 100:
                    print("1X", end="|")
            else:
                print(nums, end="|")
        print("\n", end="")
    print("")


# game

while True:
    #botinput
    botinput()

    #losscondition
    if fail in rowlist or fail in collist or fail in dialist:
        printfield()
        print("FUCK!!NO!! You lost!")
        break
    elif all(type(i) is str for i in field):
        printfield()
        print("Game over")
        break

    #print field
    printfield()

    #userinput   
    while True:
        try:
            x = int(input("number: "))
            if x in field:
                userinput(x)
                printfield()
                break
            else:
                print("not available")

        except(ValueError):
            print("not a number!")

    if match in rowlist or match in collist or match in dialist:
        print("AAAAAAAAAAAAHHHHHH!!!!!!! You won!")
        break
    elif all(type(i) is str for i in field):
        print("Game over")
        break

print("shutting down in 5...")
time.sleep(1)
print("shutting down in 4...")
time.sleep(1)
print("shutting down in 3...")
time.sleep(1)
print("shutting down in 2...")
time.sleep(1)
print("shutting down in 1...(bye!)")
time.sleep(1)


"""
yesses = ["Yes", "yes", "Y", "y", "Ya", "ya", "Yass", "yass", "1"]
noes = ["No", "no", "N", "n", "Nope", "nope", "Nah", "nah", "2"]
startwords = yesses + noes

while True:
    starter = input("Do you want to go first? Yes or No? ")
    if starter not in startwords:
        print("You failed to answer the yes/no question")
    else:
        break

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