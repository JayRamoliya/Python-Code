import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)
# print(x)

# plt.hist(x, 5) # 5 bars line
# plt.show()

y = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100) # 100 bars line
plt.show()