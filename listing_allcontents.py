import os
for dirpath,dirnames,filenames in os.walk('.'):
    print('the current path is:',dirpath)
    print('the directory names are:',dirnames)
    print('The filenames are:',filenames)
    print('*'*111)

