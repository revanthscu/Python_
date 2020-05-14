a=input("enter the string:")        #Input declaration.
s=k=d=s1=' '                            #Variable for loop
for x in a:                                # loop to check the type of input(either alphabet or digit)
    if x.isalpha():
        s=x
    else:
        s1=x
        k=k+s+chr(ord(s)+int(s1))
d=d+k
print(d)