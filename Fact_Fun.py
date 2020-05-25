def Fact(num):
	num=int(input('Enter the number whose factorial needs to be calculated:'))
	fact=1
	for i in range(1,num+1):
        	fact=fact*i
	print("The factorial of the number is:",fact)
Fact('num')

