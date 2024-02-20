# using var() methods

# Variance is another number that indicates how spread out the values are.

# Find the mean:

# For each value: find the difference from the mean:

# For each difference: find the square value:

# The variance is the average number of these squared differences:

import numpy as np

speed = [32,111,138,28,59,77,97]

# x = np.var(speed)

# standard deviation is the square root of the variance:

x = np.std(speed)
print(x)