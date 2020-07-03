class Parent:
    x=100
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def day(self):
        print('Eats and drinks',self.name,self.age)
class Child(Parent):
    x=50
    def __init__(self,color,skill,name,age):
        super().__init__(name,age)
        self.color=color
        self.skill=skill
    def disp(self):
        print('Eats and learns all day',self.color,self.skill)
c=Child('black','M','SURYA',25)
c.disp()
c.day()
