import numpy as np

a = np.arange(12)**2     # the first 12 square numbers

i = np.array([1,2,3,4,5])   # an array of indices

print(a[i])     # the elements of a at the positions i


j = np.array([[3,4], [9,7]])    # a bidimensional array

print(a[j])     # the same shape as j


# Color codes
palette = np.array([[0,0,0],
                   [255,0,0],
                   [0,255,0],
                   [0,0,255],
                   [255,255,255]])

image = np.array([[0,1,2,0],
                  [0,3,4,0]])
# each value corresponds to a color in the palette

# the (2,4,3) color image
print(palette[image])
