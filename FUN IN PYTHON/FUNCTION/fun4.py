# anonymouse function
# without name

# lambda kayword

from ast import Expression

from numpy import double


# lambda argument: Expression

double =lambda x:x*2
# print(double(5))

# filter() function
mylist=[1,5,8,3,7,4,8,5,3]
newlist=list(filter(lambda x:(x%2==0) , mylist))
print(newlist)

# map() function
new=list(map(lambda x:x*2,mylist))
print(new)