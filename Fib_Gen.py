n=int(input('Enter the number of Fibonacii :'))
def fib(n):
	i=0
	k=1
	res=0
	x=0
	while x<n:
		yield res
		i=k	
		k=res
		res=i+k
		x+=1
f=fib(n)
for i in f:
	print(i)
