#######   Fibonacci Series  ######

"""
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b
print("Done")
"""

while True:
    a = int(input("Enter the number : "))
    num = 0
    temp = a

    while temp > 0:
        r = temp % 10
        sum = sum + (r**3)
        temp = temp//10

    if(a == sum):
        print("Number is armstrong")

    else:
        print("Not armstrong")