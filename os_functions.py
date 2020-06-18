import os
from datetime import *
from os import system as s
#s('gedit')
#s('python3 Fib_Gen.py') #opens another pyhton program within the existing program.
val=os.stat('Fib_Gen.py')
print(val)
print('File size in bytes',val.st_size)
print('Last accessed time',val.st_atime)
'''os.stat_result(st_mode=33204, st_ino=799236, st_dev=2055, st_nlink=1, st_uid=1000, st_gid=1000, st_size=169, st_atime=1592487375, st_mtime=1591196527, st_ctime=1591196528'''
print('Last accessed time',datetime.fromtimestamp(val.st_atime))

