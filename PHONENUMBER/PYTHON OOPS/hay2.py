class Car:

    incr = 1.33
    def __init__(self,ty,pri,age):
        self.ty=ty #-->aa baju nu uper che e
        self.pri=pri 
        self.age=age
        self.incr=1012

    
    def incrment(self):
        # self.pri=self.pri * Car.incr #--> here Car.incr todo incr=1.33
        self.pri=self.pri * self.incr #--> here self.incr todo incr=1012
# create a object
bmw = Car("apllo",1234,100)
audi = Car("mrf",1343434,100)
farari = Car("apple",123434,100)

print(bmw.pri)
bmw.incrment()
print(bmw.pri)

print(audi.__dict__) #--> audi na all variable

print(Car.__dict__) #--> all variable show
# print(farari.pri)



# print(audi.pri)
# print(audi.ty)
# print(bmw,audi)