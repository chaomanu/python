from itertools import count, repeat

for i in count(-10):
    """ countdown """
    i *= (-1)
    print(i)
    if i == 0:
        print("*rocketenginesounds*")
        break

print("\n###\n")

child = list(repeat("mommy", 10))
for word in child:
    print(word)
print("WHAT?")

print("\n###\n")

from itertools import accumulate, takewhile

nums = list(accumulate(range(10)))
# adds the number of items in the list to the next number that is added = running total
print(nums)

def even(num):
    """ even numbers """
    if num % 2 == 0:
        return True

for num in nums:
    if even(num) is True:
        print(str(num) + " is even")
    else:
        print(str(num) + " is not even")

print(list(takewhile(lambda x: x <= 1, nums)))