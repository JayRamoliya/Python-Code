# creating pie charts

# pie() function use

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15]) # simple array

lab=['apple','mango','banana','cocunut'] # list of lable

# default start is x-axis and moves counter clock wise

# plt.pie(y) # simple chart
# plt.show() 

# plt.pie(y,labels=lab) # with label 
# plt.show() 

# plt.pie(y,labels=lab,startangle=90) # with start angle
# plt.show() 

myexp=[0.2,0,0,0] # o.2 from the center of the pie
# plt.pie(y,labels=lab,explode=myexp) # eith explode
# plt.show() 

# plt.pie(y,labels=lab,shadow=True) # shadow 
# plt.show() 

color=['r','b','g','y']
# plt.pie(y,labels=lab,startangle=90,colors=color) 
# plt.show() 
plt.pie(y,labels=lab,startangle=90,colors=color) 
plt.legend(title="four fruits")
plt.show() 

# plt.pie(y,labels=lab,startangle=90) 
# plt.show() 
