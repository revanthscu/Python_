import os
list=os.listdir()
for i in list:
    print(i)
print('The number of files in the current working directory is :',len(list))
