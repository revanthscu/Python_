from zipfile import *
f=ZipFile('zippedfiles.zip','r',ZIP_STORED)
print('Files unzipped successfully!!')
print(f.namelist())
