class Duck:
    def talk(self):
        print('quack..quackk..quackkk....')
class Dog:
    def talk(self):
        print('bow...wow...bow..wow...')
class Cat:
    def talk(self):
        print('meow..meow..meow..')
class Goat:
    def talk(self):
        print('meaaah...meahhh...meahhh')

l=[Duck(),Dog(),Cat(),Goat()]
for i in l:
    i.talk()
