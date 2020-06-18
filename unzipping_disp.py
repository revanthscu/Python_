from zipfile import *
f=ZipFile('zippedfiles.zip','r',ZIP_STORED)
content=f.namelist()
for eachfile in content:
    k=open(eachfile,'r')
    print(k.read())
    print('the contents of {} are displayed above'.format(eachfile))
print('unzipping and displaying of files are accomplished!!')
