'''
n = 8
for i in range(2,n):
    if n % i == 0:
        print(n, " is not a prime number")
        break
else:
    print(n," is a prime number")
'''
    
    
for x in range(2,50):
    for y in range(2,x):
        if x % y == 0:
            break
    else:
        print(x, " is a prime number")