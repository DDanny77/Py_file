##NESTED IF

if(False):
    print("if")
    if(True):
        print("nested if")
        if(False):
            print(1)
        elif(True):
            print(2)
        else:
            print(3)
    elif(True):
        print("nested elif")
    else:
        print("nested else")


elif(False):
    print("elif1")

elif(True):
    print("elif2")

else:
    print("else")

