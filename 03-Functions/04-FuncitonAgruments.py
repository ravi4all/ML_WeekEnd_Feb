# Required Agrs

def req( str ):
    print(str)
    return
req("This is required string")


# Keyword Args
def keyword( name, age ):
    print(name, age)
    return
keyword(name = "XYZ", age = 20)


#  Default Args

def default(name, age = 20):
    print(name, age)
    return
default("Mike")
default(name = "John", age = 22)

# Variable length Args
def length(arg1, *dynamic):
    print("Output is :")
    print(arg1)
    for var in dynamic:
        print(var)
    return
length(10)
length(20,30,40,50)