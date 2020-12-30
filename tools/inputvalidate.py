### accepts only int

def intval():
    
    try:
        while True: 
            i = int(input("input number: "))
            print("ok")
            break
    except:
        print("not a number")
        intval()

intval()

### checks if in data structure

# single type

list = ["word", "1", "2"]  # string only

def inval():
    try:
        n = input("input: ") # takes string input
        if n in list:
            print("it's in the box")
            return
        else:
            print("WHAT'S IN THE BOX?!")
            inval()
    except:
        print("something happened")
inval()


# str and int

list = ["word", "1", 2, 3]

def inval():

    try:
        n = input("str input: ") # takes string input    
        m = int(input("int input: ")) #takes int input
        if n in list:
            print("str is in the box")
            if m in list:
                print("int is in the box")
                return
            return
        elif m in list:
                print("int is in the box")
                return    
        else:
            print("not in the box")
            inval()
    except:
        print("input one string and one number")
        inval()
inval()