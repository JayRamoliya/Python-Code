from statistics import variance
from tkinter import Variable


# global variable and local Variable with same name

x="global"
def foo():
    # x=x*2  -- is  not posibal x is defing
    y='local'
    print('inside ',x)

# foo()
# print('outside ',x)
# print(y)  -- is local variable


def foos():
    global x
    y='local'
    x=x*1
    print(x)
    print(y)

# foos()

def outer():
    x='local'
    def inner():
        nonlocal x
        x='nonlocal'
        print('inner ',x)
    inner()
    print('outer ',x)

# outer()

c=1 
def add():
    # c=c+2 --only can access not a modify
    # modify will be 
    global c
    c=c+3
    print(c)
add()



