# required arguments
# def avarage(a,b):
#     print("the ",(a+b)/2)
# avarage(3,6)

# default argument
# def avarage(a=9,b=3):
#     print("the ",(a+b)/2)
# avarage()
# avarage(4,67)
# avarage(67)
# avarage(b=67)

# def name(fname,mname="jay",lname="ramoliya"):
#     print("hello,",fname,mname,lname)
# name("name")

# keyword argument
# def avarage(a,b):
#     print(a,b)
# avarage(b=3,a=6)

# required argument
# def avarage(a,b=3):
#     print("the ",(a+b)/2)
# avarage(38)

# variable-length argument
# def avage(*numbers): # puri tuple lai sakay
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average is: ",sum/len(numbers))
# avage(5,6,9,8)
# avage(5,6,934)

# def lisname(*name):
#     i=0
#     for i in name:
#         print("hello ",name)
# lisname("jay","prince")

# keyword arbitrary argument
# def names(**name): # puri dict lai sakay
#     print(type(name))
#     print("hello ",name["fname"],name["mname"],name["lname"])

# names(mname="jay",lname="ramoliya",fname="name")

def avage(*numbers): # puri tuple lai sakay
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers) #return ni value variable ma store karvi pade

# avage(4,6,8,3)
a=avage(4,6,8,3)
print(a)