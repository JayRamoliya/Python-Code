# create class
class my:
    x=133

# create object
# object name is anything
p1=my()
print(p1.x)

# __init__() function

class person:
    def __init__(self,aname,aage): 
        self.name=aname
        self.age=aage

p1=person("jay",133)
print(p1.name)