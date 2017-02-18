import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

# indices for the first dim of a
i = np.array([[0,1],
              [1,2]])

# indices for the second dim
j = np.array([[2,1],
              [3,3]])

print("--------------------------------------")
print(i)

print("--------------------------------------")
print(j)

print("--------------------------------------")
print(a[i,j])
