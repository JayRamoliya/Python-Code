# matplotlib bars

# z=np.array(range(10))
# u=np.array(range(10))

# plt.bar(z,u)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# create bars with bar()
# plt.bar(x,y)
# plt.show()

# plt.barh(x,y) # barh function display horizontal bars
# plt.show() # show the graph

# bar color

# plt.bar(x,y,color='r') # set color red
# plt.show()

# plt.bar(x,y,color='r',width=0.1) # set color red and width 0.1 default=0.8
# plt.show()

# plt.barh(x,y,color='g',height=0.1) # height 0.1 can only barh not bar color is green default is 0.8
# plt.show()