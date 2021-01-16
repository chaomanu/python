#!/usr/bin/env python

import time

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# number of fields

positions = {
1: "untenlinks",
2: "untenmitte",
3: "untenrechts",
4: "linksmitte",
5: "mittemitte",
6: "mitterechts",
7: "linksoben",
8: "mitteoben",
9: "rechtsoben"
}
# dictionary assigning names to the fields

import random

def printmatrix():
    """prints the 3x3 matrix"""
    print("", *list[7:10],"", sep = "|")
    print("", *list[4:7],"", sep = "|")
    print("", *list[1:4],"", sep = "|")

def matrixdeko(printmatrix):
    def wrap():
        print("\n")
        printmatrix()
        print("\n")
    return wrap

dekomatrix = matrixdeko(printmatrix)

### inputs

def userinput():
    """ takes userinput 1-9, replaces that position in the list with "x", prints a message and adds "c" as a counter to the list """
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
    """ let's the bot draw on a random field """
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
    """ for the most beautiful wincondition"""

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
    """ function that determines when win is triggered """
        
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
    """ function that determines when loss is triggered """

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
            list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            continue
    elif playagain in noes:
            print("OK, bye-ee!")
            time.sleep(5)
            break