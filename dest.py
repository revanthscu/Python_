import gc
import time
print(gc.isenabled())
class Test:
    def __init__(self):
        print('The constructor is executing')
    def __del__(self):
        print('Destructor is executing')
t1=Test()
t2=t1
t3=t2
del t1
print('deleting t1')
time.sleep(10)
del t2
print('Deleting t2')
time.sleep(5)
del t3
print('deleting t3')
time.sleep(2)
