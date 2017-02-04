""" Logical Operators
 Logical And, Logical OR, Logical NOT """

a = 5>4 and 4>3
print(a)

b= 4>5 or 5>4
print(b)

c = not(5>4)
print(c)


""" Membership Operators
 in, not in    """
a = 10
b = 50
c = [10,20,30,40,60]
if a in c:
    print("a is given in list")
else:
    print("a is not given")
if b not in c:
    print("b is given in list")
else:
    print("b is not given in list")
    

""" Identity Operators
 is, is not    """

d = 20
e = 20
if(d is e):
    print("Same")
else:
    print("Not same")
    
e = 10
if(d is e):
    print("Same")
else:
    print("Not same")
        