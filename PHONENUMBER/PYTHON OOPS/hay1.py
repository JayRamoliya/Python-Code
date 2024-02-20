class Car:
    def __init__(self,ty,pri):
        self.ty=ty #-->aa baju nu uper che e
        self.pri=pri 
        

# create a object
bmw = Car("apllo",10000)
audi = Car("mrf",1343434)

# --aa code lakhvani jarur nathi consturct--
# bmw.ty="apllo"
# bmw.pri=1000000

# audi.ty="mrf"
# audi.pri=2000000

print(audi.pri)
print(audi.ty)

print(bmw,audi)