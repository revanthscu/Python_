from zipfile import *
f=ZipFile('zippedfiles.zip','w',ZIP_DEFLATED)
f.write('abc.txt')
f.write('log.txt')
f.close()
print('The files zipped successfully!!')
print(f.namelist())
