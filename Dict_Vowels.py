a=input('Enter the string/name:')
b={}
c=['a','e','i','o','u']
for i in a:
        if i in c:
            b[i]=b.get(i,0)+1
for k,v in b.items():
    
    print("The vowel {} is present : {} times.".format(k,v))
