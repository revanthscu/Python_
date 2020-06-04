print("this is the second module..............................")

def f1():
	if __name__=='__main__':
		print("the module excuted as part of the code in main prog")
		print("the value of the __name__ is:",__name__)
	else:
		print('the code is executing as part of another module/program')
		print("the value of __name__ is:",__name__)

f1()
