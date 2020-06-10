'''
Viewer guidance for movie streamed online, segregated based on age group.
'''
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("Please enter your age:"))

if age<18:
    raise TooYoungException("You are too young to watch this movie")
elif age>60:
    raise TooOldException("You are too old to watch this movie")
else:
    print("You can watch this movie without any restrictions")
