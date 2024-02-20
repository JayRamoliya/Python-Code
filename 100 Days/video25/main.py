# not tuple change
# tuple are immutable
# manipulating tuples

village=("keradi","pachapipada","pedhala")
temp=list(village)

temp.append("bhadara")  #add item
# print(temp)
temp.pop(1)             #remove item
# print(temp)
temp[2]="dudhivadar"    #change item
# print(temp)
village=tuple(temp)
# print(village)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
# print(southEastAsia)

# TUPLE METHODS
# COUNT METHOD
# tuple.count(element)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# INDEX METHODS
# tuple.index(element, start, end)

Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple.index(2)
res = Tuple.index(2,2,7)
print('First occurrence of 2 is', res)