s1={1,2,5,6}
s2={3,6,7}

# Joining Sets

# print(s1.union(s2))
# print(s1,s2)

s1.update(s2)
# print(s1,s2)

s2.update(s1)
# print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
# print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2) # bane ma hase e ave
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
# print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
# print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))

# SET METHODS

"""
set are same so false
and if true
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

"""
all item in original set
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

"""
subset of original set
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

"""
add single item in set
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
# print(cities)

"""
add more than one item
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
# print(cities)

"""
remove item in set
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
# print(cities)

"""
POP()
REMOVE ANY ITEM
you assign the pop() method to a variable.
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities.pop())
# print(item)

"""
del is not a methods
is a keyword
del anything
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

"""
clear all item in set 
return empty set
"""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
# print(cities)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")