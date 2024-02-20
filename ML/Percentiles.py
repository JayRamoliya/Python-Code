# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

# using percentile() method

import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 50)
print(x)

y = np.percentile(ages, 90) # 90% of the people are younger than
print(y)