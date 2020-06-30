class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno)
        print(self.ename)
        print(self.esal)


class Increment:
    def I(val):
        val.esal=val.esal+45000
        val.display()
e=Employee(10,'Surya',30000)
Increment.I(e)
