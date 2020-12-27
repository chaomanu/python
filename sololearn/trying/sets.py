#trying sets

def spacer(x):
    print("\n" + "### " + str(x) + "\n")

spacer(1)
# lists and sets are both iterable but sets cannot be indexed since order is random

listanimals = ["wombat", "penguin", "poop"]
print(listanimals)
print(listanimals[1])
for w in listanimals:
    print(w)

setanimals = {"wombat", "penguin", "panda"}
print(setanimals)
# print(setanimals[1]) that is not possible

for w in setanimals:
    print(w)

spacer(2)
# using sets to eliminate doubles

doublelist = listanimals + listanimals
print (doublelist)

nodoubles = set(doublelist)
print(nodoubles)

spacer(3)
# turning strings into list, set, then adding items

listotheranimals = list("worm turtle seahorse".split())
listotheranimals.append("doggy")

print(listotheranimals)
setotheranimals = set("worm turtle seahorse".split())
setotheranimals.add("doggy")
print(setotheranimals) # this shows sets are unordered

spacer(4)
#turning list into set

listlol = ["poop", "pee"]
print(listlol)
setlol = set(listlol)
print(setlol)

spacer(5)
# operations

food1 = {"apples", "porridge", "cinnamon"}
food2 = {"apples", "oranges", "pears"}

print(food1 & food2) # printing only shared items #intersection
print(food1 | food2) # printing all items of both sets #union
print(food1 - food2) # pringting 1 minus items that appear in 2 #difference
print(food2 - food1) # printing 2 minus items that appear in 1 #difference

spacer(6)
#checking for an item in a set is much faster than checking for an item in a list

setthing = set("portal companioncube glados cake science".split())
setstate = set("sprinting teleporting eating crying dying doingitforsciencing".split())

thing = input("thing ")
state = input("state ")

if thing in setthing:
    print("there will be cake!")
else:
    print("the cake is gone and so are you")

if state in setstate:
    print("there will be cake!")
else:
    print("the cake is gone and so are you")