# Armstrong Number

n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
    r = temp % 10
    sum = sum + (r**3)
    temp = temp//10
if(n == sum):
    print("Armstrong")
else:
    print("Not Armstrong")