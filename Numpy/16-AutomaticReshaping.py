import numpy as np

a = np.arange(30)

a.shape = 2,-1,3    # -1 means "whatever is needed"
print(a.shape)

print(a)
