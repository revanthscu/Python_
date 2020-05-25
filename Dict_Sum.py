a=int(input("ENTER THE NUMBER OF DICT VALUES:"))
d={}

for i in range(a):
    b=input("Enter the key: ")
    c=input("Enter the value: ")
    d[b]=c
print("The original dictionary is:",d)
sum=0
sum2=''
for k,v in d.items():
    sum=sum+int(k)
    sum2=sum2+v

print("The sum of Key ","\t\t","and value are:")
print("\t\t",sum,"\t\t",sum2)
