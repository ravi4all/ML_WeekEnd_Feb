"""
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b
    print()
fib(2000)    """


# Function with return
def fib2(x):
    result = []
    a, b = 0, 1
    while b < x:
        result.append(a)
        a, b = b, a+b
    return result
    
m = fib2(100)
print(m)