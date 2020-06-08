try:
    a=int(input("Enter a number:"))
    b=int(input("Enter the second number:"))
    print(a/b)
    ''' 
except :
    print("pls provide valid input")---Default except block should be declared in the end 
    ;''' 
except (ZeroDivisionError,ValueError,TypeError) as msg:
    print("Exception handling is working:",msg)
