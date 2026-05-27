# recursion happens when a function calls itself (recursive function)
def add_one(num):
    if(num >= 9):
        # return num + 1
    
        total = num + 1
        print(total)

    return add_one(total)       #Recursive call to the function

add_one(0)

