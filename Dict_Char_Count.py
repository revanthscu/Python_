a=input("Enter the string:")
b={}
for x in a:
    b[x]=b.get(x,0)+1

print(b)  #dictionary form

for k,v in sorted(b.items()):
    print("The number of occurances of : ",k,"is:",v)
