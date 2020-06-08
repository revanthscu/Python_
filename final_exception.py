import os
try:
    print('try block')
    os._exit(0)
    '''
    particular case when finally block will not be executed!! if the JVM is shut down using os exit command
    '''
except: print('exception occured')
finally: print('this prog executed finally block')
