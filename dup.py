a=input("enter the string:")
d=[]

for x in a:
    if x not in d:
        d.append(x)

print(d)