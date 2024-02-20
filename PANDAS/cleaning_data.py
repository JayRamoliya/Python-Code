"""
Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates
"""

"""
Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.
"""
import pandas as pd

df = pd.read_csv('data.csv')

# new_df = df.dropna()
# print(new_df.to_string()) 

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument

# df.dropna(inplace = True)
# print(df.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.