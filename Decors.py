def decorat(x):
	def inner(name):
		if name=='Sachin':
			print("you are the God of cricket",name)
		else:
			x(name)
	return inner
def wish(name):
	print("Have a great day",name," You rock!!")
decorfunction=decorat(wish)

wish('surya')
wish('Jason')
wish('Sachin')
decorfunction('Sachin')

