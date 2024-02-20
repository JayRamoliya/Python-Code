# Normal Data Distribution

# In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

# We specify that the mean value is 5.0, and the standard deviation is 1.0.

# Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.

# And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
# A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.