import csv
f=open('sur_exmp.csv','r')
r=csv.reader(f)
data=list(r)
print(data)
for line in data:
    for word in line:
        print(word,'\t',end="")
    print()    
