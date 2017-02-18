import numpy as np

a = np.array([2,3,4,5])
b = np.array([3,5,2,7])
c = np.array([5,6,7,2])

ax, bx, cx = np.ix_(a,b,c)

print("------------------------------")
print(ax)

print("------------------------------")
print(bx)

print("------------------------------")
print(cx)


result = ax+bx+cx
print(result)

print(a[3]+b[2]*c[3])
