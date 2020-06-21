class Student:
    '''THis is the student class with required data!!'''
    def __init__(self,rollno,name,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
    def disp(self):
        print(self.rollno,self.name,self.marks)
a=Student(154,'Surya',100)
a.disp()
b=Student(100,'Akshitha',99)
b.disp()
print(a.__doc__)
help(Student)
