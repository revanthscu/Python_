class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.b1=30
    def m1(self):
        self.c=40
        Test.d=50
    
    @classmethod
    def m2(cls):
        cls.e=60
        Test.f=70
    
    @staticmethod
    def m3():
        Test.g=80
    
Test.h=1000
a=Test()
a.m1()
a.m2()
a.m3()
print(Test.__dict__)
