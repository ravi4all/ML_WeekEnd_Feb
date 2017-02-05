total = 0   #    Global Variable

def add(a, b):
    total = a + b       # Here, total is a local variable
    print("Total is ",total)
    return total

add(2,3)
print("Total is ",total)