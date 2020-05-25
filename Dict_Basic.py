d={}
while True:
    a=input('Enter the student name:')
    b=input("Enter the student's marks:")
    d[a]=b
    f=input("Do you want to enter another credentials(Yes/No):")
    if f=='Yes':
        continue
    else:
        break
while True:
    print("THE ORIGINAL DICT IS:",d)
    f=input("Enter the student name whose details are required:")
    k=d.get(f,-1)
    if k==-1:
        print("Student is not available")
    else:
        print("the Marks of",f,"are",k)
    f=input("please enter if you need more info (Yes/No): ")
    if f=='No':
        break
print("Thanks for using this application !!")
