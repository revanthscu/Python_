print("welcome to exceptions concept:")
try: print(10/0)
except  ZeroDivisionError:
    print("you cannot divide a numeric by char")
except  TypeError:
    print("please enter an integer")
print('this is a graceful termination of the program')
