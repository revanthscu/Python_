import csv
with open('sur_exmp.csv','w') as f:
    w=csv.writer(f)
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n=int(input('Enter the number of employees:'))
    for i in range(n):
        eno=int(input('enter the eno:'))
        ename=input('enter the ename:')
        esal=float(input('enter the salary:'))
        eaddr=input('enter the city')
        w.writerow([eno,ename,esal,eaddr])
print('the data written to csv successfully')
