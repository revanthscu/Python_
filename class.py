class STUDENT:
    def __init__(self,sid,sname,ssex,sbgroup,sloc):
        self.sid=sid
        self.sname=sname
        self.ssex=ssex
        self.sbgroup=sbgroup
        self.sloc=sloc
s=STUDENT(747,'surya','M','B+','Bangalore')
print(s.sid,s.sname,s.ssex,s.sbgroup,s.sloc)
