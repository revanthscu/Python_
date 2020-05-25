def Sum_Sub(a,b):
	sum=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return sum,sub,mul,div
t=Sum_Sub(12,4)   
'''tuple packing done into variable "t".'''
for i in t:
	print('The result of operations are: {}'.format(i))
