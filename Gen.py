

def geni(i):
	x=1
	while (x<=i):
		yield x
		x+=1

h=geni(1000000000)
for x in h:
	print(x)
