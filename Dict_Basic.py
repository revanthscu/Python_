n=int(input("Enter the number of students:"))
d={}
i=1
while i<=n:
    name=input("Enter the name of the student:")
    marks=input("Enter the marks of the student:")
    d[name]=marks
    i=i+1
print("The name of the student","\t" ,"marks is:")
for x in d:
    print("\t", x ,"\t\t", d[x])