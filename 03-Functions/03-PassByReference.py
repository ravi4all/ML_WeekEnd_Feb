#  All parameters (arguments) in the Python language are passed by reference
"""
def passMe(list):
    list.append([5,6,7,8])
    return

list = [1,2,3,4]
passMe(list)
print(list)
"""

# argument is being passed by reference and the reference is being overwritten inside the called function.
def passBy(myList):
    print("Before Updating : ",myList)
    myList = [1,2,3,4]
    print("After Updating : ",myList)
    return

myList = [5,6,7,8]
passBy(myList)
print(myList)