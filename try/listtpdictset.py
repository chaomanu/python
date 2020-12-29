### lists
#lists are iterable (can return items one at a time)
#lists are mutable (can be changed)
#lists can be indexed

print("\nlists:")
emptylist = []
numlist = [1,2,3]
print(numlist)

#index
print("first item: ", end="")
print(numlist[0])

# len
print("lenght: ", end="")
print(len(numlist))

# add
emptylist.append("notempty") # .append adds item
newlist = emptylist
print(newlist)

#insert
numlist.insert(1,0.5)
print(numlist)

#remove
numlist.remove(0.5)
print(numlist)

#reassign
numlist[0] = "first"
print(numlist)

#in
print(2 in numlist)

#matrix
print("matrix:")
matrixlist = [
[1,2,3],
[4,5,6]
]
print(matrixlist[0][0]) #first
print(matrixlist[1][2]) #last
print(matrixlist[0]) #upperrow
print(matrixlist[1]) #lowerrow

#slices
print("slices:")
listslice = [0,1,2,3,4,5]
print(listslice[0:])
print(listslice[:5])
print(listslice[1:4])

# more list stuff
print("morestuff:")
morelist = [1,2,3,4,5]
print(max(morelist)) # max value
print(min(morelist)) # min value
print(morelist.count(3)) # counts numer of occurances
morelist.reverse() # reverses list
print(morelist) #prints reversed list



### tuples
# tuples are immutable, items cannot be changed
# tuples can be used with dictionaries with tuples representing the keys that are immutable
# tuples can be indexed

print("\ntuples:")

emptytp = ()
numtp = (1,2,3)
anotherwaytodothis = 1,2,3
print(numtp)

#index
print("first item: ", end="")
print(numtp[0])

#len
print("lenght: ", end="")
print(len(numtp))

#in
print(2 in numtp)

#reassign
print("cannot reassign because tuples are immutable")


### dictionaries
# dictionaries are mutable (item values can be changed
# dictionaries can be indexed (per key)

print("\ndictionaries:")
emptydict = {}
numdict = {"first": 1, "second": 2, "third": 3}
print(numdict)

#index
print("first item: ", end="")
print(numdict["first"])

#len
print("lenght: ", end="")
print(len(numdict))

# add

numdict["forth"] = 4
print(numdict)

#reassign
numdict["first"] = "first"
print(numdict)

#in
print("second" in numdict)
print(2 in numdict)

#get
print(numdict.get("third", "not in dict"))
print(numdict.get("tenth", "not in dict"))


### sets
# sets cannot be indexed since they are unordered

print("\nsets:")
emptyset = set()
numset = {1,2,3} 
print(numset)

# index not possible
print("can't print first item")

#len
print("lenght: ", end="")
print(len(numset))

# add
emptyset.add("notempty") # .add adds item
newset = emptyset
print(newset)

# remove
numset.remove(3) # removes specific item by name not position since sets are unordered
print(numset)
numset.pop() # removes random item
print(numset)

#in
print(2 in numset)