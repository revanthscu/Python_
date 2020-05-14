a=input("enter the string:")
d={}
for x in a:
	if x not in d.keys():
		d[x]=1
	else:
		d[x]=d[x]+1
print(d)