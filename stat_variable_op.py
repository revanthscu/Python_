class Rank:
    a=100
    def __init__(self):
       self.b=10

t=Rank()
t2=Rank()
t.a=450
t.c=200
print(t.__dict__)
print(t2.__dict__)
