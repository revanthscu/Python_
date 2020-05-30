def isevn(x):
	if x%2==0:
		return True
	else:
		return False

l=[1,223,12,43,45,22,66,776,2,-6,334,333]
k=list(filter(isevn,l))
print(k)

