# tuples ()
# ordered and unchangeable.
# allow duplicate values.
# immutable and cannot be modified once they are created
# Tuples are commonly used to group related data together. 

# different data types
tup=(1,3,3,133,143,9,8,2,5)

# length of tuple
print("Length :", len(tup))

# tuple with one item
singleTup = (7,)  # (comma is required after single value for it not considered as
print(type(singleTup))

# type of tuple
thistuple = ("apple") # this is str not a tuple
print(type(thistuple))

# tuple constructor to make a tuple
mytuple = tuple(("apple","banana"))  
print(type(mytuple))

count=tup.count(3)
print(count)
# print(tup.count(3))

index=tup.index(133) #  find the index of the first occurrence of a specified element in a tuple. 
print(index)
# print(tup.index(133))

length=len(tup) #  get the length of a tuple. 
print(length)
# print(len(tup))

sorted_tup=sorted(tup) #  new sorted tuple from an existing tuple. 
print(sorted_tup)
# print(tup)
# print(sorted(tup))

# print(max(tup))
# print(min(tup))