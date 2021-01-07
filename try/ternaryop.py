import random
x = random.randint(1,6)

# two dice with even numbers showing the same face
y = (x+x) if x > 1 else 1
print(y)

# two dice with odd numbers showing the same face
y = (x+x-1) if x > 1 else 1
print(y)

# two dice
y = x + random.randint(1,6) if x > 1 else 1
print(y)