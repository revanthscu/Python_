import gc
class Person:
    def __init__(self):
        self.name='Surya'
        self.dob=self.Dob()
        self.skill=self.Skill()
        print('person object created')
    def display(self):
        print('Name',self.name)
        
    class Dob:
        def __init__(self):
            self.dd=6
            self.mm=1
            self.yy=1995
            print('dob object created')
        def display(self):
            print('DOB: {}/{}/{}'.format(self.dd,self.mm,self.yy))

    class Skill:
        def __init__(self):
            self.s='Coding'
            print('skill object created')
        def display(self):
            print('Skill:',self.s)

a=Person()
a.display()
a.dob.display()
a.skill.display()
print(gc.isenabled())
