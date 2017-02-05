# Open a file
file_open = open("demo.txt", "wb")
print("Name is ",file_open.name)
print("Opening Mode is ",file_open.mode)

# Closing a file
file_open.close()