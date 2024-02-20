# simple list
# tuple no change
# list is change
# list index positive negative

lis=["jay",133,True,34.3]

l=[3,4,5,44,6]
print(len(l))
# print(l)
# print(type(l))

# print(l[0])
# print(l[1])
# print(l[2])

# print(l[-2])
# print(l[-1])
# print(l[0])

# easy way
# print(l[-2]) #negative index
# print(l[len(l)-2]) #positive index
# print(l[3]) #positive index

# print(l[334]) # error

# if 3 in l:
#     print("yes")
# else:
#     print("no")

# same thing applies for string as well
# if "ram" in "ramoliya":
#     print("yes")

# print(l)
# print(l[0:])
# print(l[0:5])
# print(l[::2])


# list comprehension
# List=[Expression(item) for item in iterable if condition]

names=["jay","milo","rosa","bruno","prince"]
names_with0=[item for item in names if "o" in item]
print(names_with0)

names_with4=[item for item in names if (len(item)>4)]
print(names_with4)


# lst=[i*i for i in range(10)]
# print(lst)
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)
