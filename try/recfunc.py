# recursive functions
# recursion means the function is calling itself
# an explicit return statement immediately terminates a function execution and sends the return value back to the caller code

num = int(input("Input number: "))

x = 0
y = 1

def fib(n,x,y):
    """ prints the first n numbers of the fibonacci sequence """
    print(x)
    x, y = y, x+y
    n -= 1

    if n < 1:
        print("STOP")
        return #returns None

    else:
        fib(n,x,y)
    
fib(num,x,y)