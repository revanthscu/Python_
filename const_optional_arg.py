class Student:
    def __init__(self,name='',marks=0):
        self.name=name
        self.marks=marks
    def display(self):
        print('The name is :',self.name)
        print('The marks is :',self.marks)
s1=Student('SURYA',100)
s1.display()
