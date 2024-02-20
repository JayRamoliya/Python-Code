# python program to find the square root

# solution-1 (using Exponentiation)

num=64
sr=num**(1/2)
print("the square root of the given number is",sr)

# solution-2 (using math module)

import math  # importing the math library for sqrt() function.
num = int(input('Enter a positive integer: '))  
sr=math.sqrt(num)

print(sr)
