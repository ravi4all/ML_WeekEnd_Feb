"""
square = [4,25,36,48,64]
print(square)

print(square[2])        # Indexing

print(square[1:4])      # Slicing returns the new list

print(square[:3])       

print(square + [81,100,121])        # Concatenation

square[3]= 49
print(square)     # Unlike strings, which are immutable, lists are a mutable type

square.append(12**2)  
print(square)       # Append the item in last

square[2:5] = []
print(square)       # Remove the elements from 2(included) to 5(excluded)

square[:] = []
print(square)       # Empty the list

print(len(square))  # Length of list

square = [4,9,16,25]
cube = [2**3,3**3,4**3]
result = [square,cube]      # Nesting List
print(result)
"""

s = [1,2,3,4,5,6,7]
t = [11,12,13,14,15,16,17]
r= [[s,t]]
for i in r:
    print(i)