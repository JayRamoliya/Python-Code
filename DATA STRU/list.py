# lists []
# ordered, changeable, allow duplicate value
# can store collections of items
# ordered sequence of elements
# you can modified after they are created

# you can add different data type
name=['jay','heet','harsh','yesh','vani']

# list built-in methods

# length of a list
# print(len(name))

# type of list
# print(type(name))

# add elements to the end of a list
# name.append('jay') 
# print(name)

# list constructor when creating a new list
newlist = list(('apple', 'banana', 'cherry'))
# print(type(newlist))

# removes all the elements from a list
# print(newlist.clear())

# return a copy of the list
# copy_of_lst = newlist.copy()

# count how many times an item appears in the list
# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# print(points.count(9))

# adds the specified list elements (or any iterable) to the end of the current list.
# name.extend(points)
# print(name)

# return elements index of first occurrence of the value
# print(name.index('jay'))

# add elements to a specific index in the list
# name.insert(1,'ram') 
# print(name)

# the first occurrence of an element in the list. 
# name.remove('jay') 
# print(name)

# Removes and returns the element at a specific index in the list.
# pop=name.pop(1)
# print(name)
# print(pop)

# the elements in the list in ascending order. 
# reverse=True will sort the list descending. Default is reverse=False
# key --> A function to specify the sorting criteria(s)
x=[1,133,1,3,9,8]
# print(x.sort(reverse=True))


# the order of the elements in the list. 
name.reverse() 
# print(name)

# list comprehensions
squares=[[x**2] for x in range(1,5)]
# print(squares)

num=[1,2,3,4,5,6,7]
even_num=[x for x in num if x % 2 ==0]
# print(even_num)

# lengths=[len(name) for name in name]
# print(lengths)

# access list items

print(name[1])
print("last item :",name[-1])
print(name[2:4]) # 4 is not included