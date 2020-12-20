beginner = input("Do you want to be the beginner? Yes or No?")
yesses = ["Yes", "yes", "Y", "y", "Ya", "ya", "Yass", "yass"]
noes = ["No", "no", "N", "n", "Nope", "nope", "Nah", "nah"]

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
    print(*list[7:10], sep = " ")
    print(*list[4:7], sep = " ")
    print(*list[1:4], sep = " ")

def wincondition():
        
        if list[7] == "x" and list[8] == "x" and list[9] =="x" or list[4] == "x" and list[5] == "x" and list[6] =="x" or list[1] == "x" and list[2] == "x" and list[3] =="x":
            return True
        elif list[7] == "x" and list[4] == "x" and list[1] =="x" or list[8] == "x" and list[5] == "x" and list[2] =="x" or list[9] == "x" and list[6] == "x" and list[3] =="x":
            return True
        elif list[1] == "x" and list[5] == "x" and list[9] =="x" or list[7] == "x" and list[5] == "x" and list[3] =="x":
            return True
        else:
            return False

def losscondition():

        if list[7] == "o" and list[8] == "o" and list[9] =="o" or list[4] == "o" and list[5] == "o" and list[6] =="o" or list[1] == "o" and list[2] == "o" and list[3] =="o":
            return True
        elif list[7] == "o" and list[4] == "o" and list[1] =="o" or list[8] == "o" and list[5] == "o" and list[2] =="o" or list[9] == "o" and list[6] == "o" and list[3] =="o":
            return True
        elif list[1] == "o" and list[5] == "o" and list[9] =="o" or list[7] == "o" and list[5] == "o" and list[3] =="o":
            return True
        else:
            return False

if beginner in yesses:
    for number in list:    

        x=int(input("Please input 1-9"))
        if x in list:    
            print("you draw x at " + str(x) + " " + positions[x])
            list[x] = "x"
            list.append("c")

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

elif beginner in noes:
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

        x=int(input("Please input 1-9"))
        if x in list:    
            print("you draw x at " + str(x) + " " + positions[x])
            list[x] = "x"
            list.append("c")

        if wincondition() == True:
            printmatrix()
            print("You won! Suck it, randobot!")
            break

    print("Game over")    

else:
    print("You failed to answer the yes or no question")   

