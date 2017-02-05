def disp(msg):
    
    def nested_disp():
        print(msg)
    nested_disp()
        
disp("This is going to be display")

"""
def disp(msg):
    
    def nested_disp():
        print(msg)
    return nested_disp
        
caller = disp("This is going to be display")
caller()
"""