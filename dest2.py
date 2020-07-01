import sys
import time
class Test:
    def __init__(self):
        print('constructor executing')
    def __del__(self):
        print('destructor executing')
a=Test()
b=a
c=b
d=c
time.sleep(5)
print(sys.getrefcount(a))
del a
