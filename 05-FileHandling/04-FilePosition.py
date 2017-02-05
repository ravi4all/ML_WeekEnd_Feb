# Open a File
a = open("demo1.txt", "r+")
str = a.read(10)
print(str)

pos = a.tell()
print("Position is ",pos)

# Reposition pointer at the beginning once again
position = a.seek(10, 0);
str = a.read(10);
print ("Again read String is : ", str)

# Close file
a.close()