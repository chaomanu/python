starting = input("Do you want to start? Yes or No?")
yesses = ["Yes", "yes", "Y", "y", "Ya", "ya", "Yass", "yass", " Yes", " yes"]
noes = ["No", "no", "N", "n", "Nope", "nope", "Nah", "nah", " No", " no"]

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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

import random

def printmatrix():
    print("", *list[7:10],"", sep = "|")
    print("", *list[4:7],"", sep = "|")
    print("", *list[1:4],"", sep = "|")

def userinput():
    try:
        x=int(input("Please input 1-9"))
        if x in list:    
            print("you draw x at " + str(x) + " " + positions[x])
            list[x] = "x"
            list.append("c")
        else:
            print("that...was not a valid input")
    except ValueError:
        print("that...was not a valid input")

def wincondition():
    row1 = list[1:4]
    row2 = list[4:7]
    row3 = list[7:10]
    col1 = list[1:8:3]
    col2 = list[2:9:3]
    col3 = list[3:10:3]
    dia1 = list[1:10:4]
    dia2 = list[3:8:2]
        
    if row1 == ["x","x","x"] or row2 == ["x","x","x"] or row3 == ["x","x","x"]:
        return True
    elif col1 == ["x","x","x"] or col2 == ["x","x","x"] or col3 == ["x","x","x"]:
        return True
    elif dia1 == ["x","x","x"] or dia2 == ["x","x","x"]:
        return True

def losscondition():

        if list[7] == "o" and list[8] == "o" and list[9] =="o" or list[4] == "o" and list[5] == "o" and list[6] =="o" or list[1] == "o" and list[2] == "o" and list[3] =="o":
            return True
        elif list[7] == "o" and list[4] == "o" and list[1] =="o" or list[8] == "o" and list[5] == "o" and list[2] =="o" or list[9] == "o" and list[6] == "o" and list[3] =="o":
            return True
        elif list[1] == "o" and list[5] == "o" and list[9] =="o" or list[7] == "o" and list[5] == "o" and list[3] =="o":
            return True

if starting in yesses:
    
    printmatrix()
    
    for number in list:    
        
        userinput()

        if wincondition() == True:
            printmatrix()
            print("You won! Suck it, randobot!")
            break
        
        o = random.randint(1,9)
        
        while o not in list and len(list) < 19:
            o = random.randint(1,9)
        if o in list:
            print("randobot draws o at " + str(o) + " " + positions[o])
            list[o] = "o"
            list.append("c")
        
        printmatrix()

        if losscondition() == True:
            print("Oh no! You got owned by randobot!")
            break  

        if len(list) > 18:
            print("No winner! (lame)")
            break

    print("Game over")

elif starting in noes:
    for number in list:

        o = random.randint(1,9)
        
        while o not in list:
            o = random.randint(1,9)
        if o in list:
            print("randobot draws o at " + str(o) + " " + positions[o])
            list[o] = "o"
            list.append("c")

        printmatrix()

        if losscondition() == True:
            print("Oh no! You got owned by randobot!")
            break

        if len(list) > 18:
            print("No winner! (lame)")
            break

        userinput()

        if wincondition() == True:
            printmatrix()
            print("You won! Suck it, randobot!")
            break

    print("Game over")    

else:
    print("You failed to answer the yes or no question")   

