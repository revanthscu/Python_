a=input("enter the string:")
c=[]
s=[]
h=len(a)
for x in a:
    
    if x not in c:
        c.append(x)
        s.append(a.count(x,0,len(a)))
for i in range(len(c)):
    print("The count of char : {} is:{}".format(c[i],s[i]))
    i+=1
	