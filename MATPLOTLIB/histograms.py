# Histograms

# hist() function to create

import matplotlib.pyplot as plt
import numpy as np


x = np.random.normal(170, 10, 250) # this is a normal  data distribution 

plt.hist(x)
plt.show()