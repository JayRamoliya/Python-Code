# Median - The mid point value

# It is important that the numbers are sorted before you can find the median.

# use median() methods

import numpy as np

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = np.median(speed)
print(x)

# If there are two numbers in the middle, divide the sum of those numbers by two.