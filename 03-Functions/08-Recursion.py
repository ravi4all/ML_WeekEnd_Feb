def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
num = 5
print("Factorial of ", num, "is", factorial(num))  