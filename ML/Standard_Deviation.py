# Standard deviation is a number that describes how spread out the values are.

# A low standard deviation means that most of the numbers are close to the mean (average) value.

# A high standard deviation means that the values are spread out over a wider range.

# using std() methods

import numpy as np
# speed = [86,87,88,86,87,85,86] # low

speed = [32,111,138,28,59,77,97] # high

x = np.std(speed)
print(x)