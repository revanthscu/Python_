class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def carInfo(self):
        print('name is :{} model is:{} color is:{}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self,eno,ename,car):
        self.eno=eno
        self.ename=ename
        self.car=car
    def empInfo(self):
        print('The eno is {} and name is {}'.format(self.eno,self.ename))
        print('The details of the car is:')
        self.car.carInfo()
c=Car('BMW','X7','White')
e=Employee(154,'Surya',c)
e.empInfo()
