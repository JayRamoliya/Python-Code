# print(module.__doc__)


# def function_name(parameter):
#     """docstring"""
#     statement(s)

# def greet(name):
#     """this function greet to
#     the person passed in as 
#     a parameter"""
#     print('hello ',name,' good morning')

# greet('jay')
# print the docstring
# print(greet.__doc__)

# print(print.__doc__)


def value(num):
    """
    this function return the absolut value 
    of the entered number
    """
    x=10
    print("value inside ",x)
    if num>=0:
        return num
    else:
        return -num

x=20
value(1)
print(value(2))
print(value(-4))
print('value outside ',x)



