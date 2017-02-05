# If you do need to iterate over a sequence of numbers, range() comes in handy. It generates arithmetic progressions:

for i in range(10):
    print(i)
    
a = ['abc','def','ghi','jklmno']
for i in a:
    print(i, len(i))
    
for i in range(len(a)):
    print(i,a[i])   # To iterate over the indices of a sequence, you can combine range() and len()
    
print(range((10)))