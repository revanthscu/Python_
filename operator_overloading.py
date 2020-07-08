class Book:
    def __init__(self,pages):
        self.pages=pages
    #defining magic methods
    def __add__(self,other):
        return self.pages+other.pages
    def __gt__(self,other):
        return self.pages>other.pages
    def __sub__(self,other):
        return  self.pages-other.pages
    def __le__(self,other):
        return self.pages<=other.pages

a=Book(100)
b=Book(200)
print('The sum of the pages are:',a+b)
print('Is a greater than b?:',a>b)
print('The subtraction of a,b is:',a-b)
print('Is a less than or equal to b?:',a<=b)
