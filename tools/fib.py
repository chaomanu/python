# for loop

num = int(input("print the first n numbers of the fibonacci sequence, input n: "))

def fibonacci(n):

    x, y = 0, 1
    print(x)   

    for n in range(1,n):
        x, y = y, x + y
        print(x)
    
fibonacci(num)


print("")


# recursive function

num = int(input("print the first n numbers of the fibonacci sequence, input n: "))

x, y = 0, 1

def fib(n,x,y):
    
    print(x)
    x, y = y, x+y
    n -= 1

    if n < 1:
        return

    else:
        fib(n,x,y)
    
fib(num,x,y)