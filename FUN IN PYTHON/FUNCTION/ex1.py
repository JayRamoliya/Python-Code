from ast import arg
from unittest import result

# creat function

def demo(name,age):
    print(name,age)

# demo('jay',19)

# Return multiple values from a function

def func1(*args):
    for i in args:
        print(i)
# func1(2,3,45)
# func1(45,56,5,5,5,3)

# Return multiple values from a function

def calcu(a,b):
    add=a+b
    sub=a-b
    return add,sub
    # return a+b,a-b  or 
res=calcu(40,10)
# print(res)

# Create an inner function to calculate the addition in the following way

def out(a,b):
    squre=a**2

    def addi(a,b):
        return a+b

    additions=addi(a,b)
    return additions+5
    
result=out(5,10)
print(result)