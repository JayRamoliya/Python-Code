# A Pandas DataFrame is a 2 dimensional data structure,

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df) 

# locate row
#refer to the row index:
# print(df.loc[0])

#use a list of indexes:
# print(df.loc[[0, 1]])

# named indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 

# locate named indexes
# print(df.loc['day2']) # print row 2
# print(df.loc['day1']) # orint row 1

# Load Files Into a DataFrame
df = pd.read_csv('data.csv')
print(df) 
