def K(**kwargs):
	print(type(kwargs))
	print("The values are:")
	for k,v in kwargs.items():
		print(k,"..............................",v)
K(name="surya",marks=100,coll="SCU",GF="None")
K(name='Aish',nature='kid',artist_level='Pro',sal=300000000)
