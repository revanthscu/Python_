a=input("Enter the string of your choice:")			#input string having multiple characters.
d={}																	#dictionary declaration.
for x in a:
	if x not in d.keys():
		d[x]=1
	else:
		d[x]=d[x]+1
for k,v in d.items():
    print("character: {} occures: {} times.".format(k,v))