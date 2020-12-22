starter = input("Do you want to go first? Yes or No? ")
yesses = ["Yes", "yes", "Y", "y", "Ya", "ya", "Yass", "yass", "1"]
noes = ["No", "no", "N", "n", "Nope", "nope", "Nah", "nah", "2"]
# determines who goes first - player or bot

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# number of fields, not scalable as of now

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

def boom():
    """ easteregg win message if 2 lines are completed """
    print("BOOM!")
    print("tetris for jeff")

def win():
    """ win message """
    print("You won! Suck it, randobot!")

# win and loss conditions start here

def winpretty():
    """ for the most beautiful wincondition"""

    row2 = list[4:7]
    col2 = list[2:9:3]

    trix = ["x", "x", "x"] 
    trio = ["o", "o", "o"]

    if (row2 == trix and col2 == trix):
        return True
    elif (row2 == trio and col2 == trio):
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



# beginning of the game

if starter in yesses:
# if the player has first turn

    print("\n")
    printmatrix()
    print("\n")
    # prints matrix

    for number in list:  
    # for loop that first takes userinput, checks wincondition, takes botinput, prints matrix again, checks losscondition, checks if draw 
        
        userinput()

        if winboom() == True:
            print("\n")
            printmatrix()
            print("\n")
            boom()
            print("\n")
            if winpretty() == True:
                print("omg so pretty")
                print("\n")
            win()
            break

        elif wincondition() == True:
            print("\n")
            printmatrix()
            print("\n")
            win()
            break
        
        o = random.randint(1,9)
        
        while o not in list and len(list) < 19:
            o = random.randint(1,9)
        if o in list:
            print("randobot draws o at " + str(o) + " " + positions[o])
            list[o] = "o"
            list.append("c")
    
        print("\n")
        printmatrix()
        print("\n")

        if losscondition() == True:
            if winpretty() == True:
                print("omg so pretty")
                print("\n")
            print("Oh no! You got owned by randobot!")
            break  

        if len(list) > 18:
            print("No winner! (lame)") 
            break

    print("Game over")
    # prints Game over after loop break

elif starter in noes:
# if the bot has first turn

    print("\n")
    for number in list:
    # for loop that takes botinput, prints matrix, checks losscondition, checks if draw, takes userinput, checks wincondition

        o = random.randint(1,9)
        
        while o not in list:
            o = random.randint(1,9)
        if o in list:
            print("randobot draws o at " + str(o) + " " + positions[o])
            list[o] = "o"
            list.append("c")

        print("\n")
        printmatrix()
        print("\n")

        if losscondition() == True:
            if winpretty() == True:
                print("omg so pretty")
                print("\n")
            print("Oh no! You got owned by randobot!")
            break

        if len(list) > 18:
            print("No winner! (lame)")
            break

        userinput()

        if winboom() == True:
            print("\n")
            printmatrix()
            print("\n")
            boom()
            print("\n")
            if winpretty() == True:
                print("omg so pretty")
                print("\n")
            win()
            break

        elif wincondition() == True:
            print("\n")
            printmatrix()
            print("\n")
            win()
            break

    print("Game over")    

else:
    print("You failed to answer the yes or no question")
    # if the user didn't provide a yes no answer