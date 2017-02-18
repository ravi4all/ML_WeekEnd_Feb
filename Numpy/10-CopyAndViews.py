import numpy as np

a = np.arange(12)

# No Copy at All
print("No Copy at All")
b = a           # no new object is created
print(b is a)
# a and b are two names for the same ndarray object

b.shape = 3,4 # changes the shape of a
print("Shape of B",b.shape)
print("Shape of A",a.shape)



# View or Shallow copy
print("View or Shallow copy")
c = a.view()
print(c is a)

print(c.base is a)       # c is a view of the data owned by a

c.shape = 2,6   # a's shape doesn't change
print("Shape of C",c.shape)
print("Shape of A",a.shape)

c[0,4] = 1234
print("A's data will change")
print(a)        # a's data will change


# Deep Copy
d = a.copy()     # a new array object with new data is created
print("Deep Copy")
print(d is a)

print(d.base is a)   # d doesn't share anything with a

d[0,1] = 1000
print(a)
