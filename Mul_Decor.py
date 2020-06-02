def decor(abc):
	def inner(name):
		if name=='surya':
			print("have an ossom morning",name)
			print("this is the first decorator executing!!!")
		else:
			abc(name)
	return inner

def decor2(asa):
	def inner(name):
		print("this is the second decorator execuing!!!")
		asa(name)
	return inner



@decor2
@decor
def wish(name):
	print("hello",name,"you rock!!!")


wish('aish')
