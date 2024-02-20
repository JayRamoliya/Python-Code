# shift + rclick
# pip install pandas
# pip install numpy
# pip install --upgrade pandas

import numpy as np
import pandas as pd

dict1={
    'Name':['John','Emma',np.nan,'Michael'],
    "Age":[25,30,45,67],
    "City":["New York","London",None,"Paris"],
}
df=pd.DataFrame(dict1)
df.to_csv('friends.csv') # ,index=False not add index in csv file

# print(pd.DataFrame(dict1))

# print(df.head(2)) # head is start 2 index show

# print(df.tail(1)) # head is last 1 index show

# print(df.describe()) # num value ne count, mean, std, min, max, 25%, 50%, ...

jay=pd.read_excel('data.xlsx')
# print(jay) # all data is show
# print(jay['trainno']) # only show train no
# print(jay['speed']) # only show speed
# print(jay['city']) # only show city

# print(jay['city'][0]) # show city index 0
# print(jay['trainno'][2]) # show speed index 2
# print(jay['speed'][1]) # show speed index 1

# jay['city'][0]='keradi' # change value of index 0 
# jay['trainno'][0]=1 # change value of index 0 
# jay['speed'][0]=100 # change value of index 0 

# print(jay['speed'][0]) # warning show thsse

# jay.to_csv('jay.csv')
# jay.index=['first','second','third','fourth'] # change index to anything use it
# print(jay)

