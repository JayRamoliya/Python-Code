class employe:
    def __init__(self,aname,aid):
        self.id=aid
        self.name=aname

    def display(self):
        print("id: %d\nname: %s"%(self.id,self.name))

emp1=employe("jay",133)

emp1.display()