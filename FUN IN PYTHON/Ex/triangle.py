from numpy import mat
import math

a=float(input('enter the length of side a: '))
b=float(input('enter the length of side b: '))
c=float(input('enter the length of side c: '))

s=(a+b+c)/2

area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area of the traangle is: ',area)