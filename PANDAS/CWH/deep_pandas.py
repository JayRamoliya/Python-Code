# data analysis library 

# pandas two data structure

# series --> one dimensional array with indexes.

# dataframe --> two dimensional data 

import numpy as np
import pandas as pd

ser=pd.Series(np.random.rand(10))
# print(ser) # random value
# print(type(ser)) # pandas.core.series.Series

df=pd.DataFrame(np.random.rand(10,5),index=np.arange(10))
# print(df) # show dataframe
# print(type(df)) # pandas.core.frame.DataFrame

# print(df.dtypes) # data type in each column

# print(df.head(5))

df[0][0]="jay"
# print(df.dtypes)

# print(df.index) # show index
# print(df.columns) # show columns

# print(df.to_numpy()) # convert to array

# print(df.T) # trans pos row -> column

# print(df.sort_index(axis=0,ascending=False)) # sort axis 0 is rows and ascending is byd is true

# print(df.sort_index(axis=1,ascending=False)) # column axis 1 is column

newdf=df # newdf is view of df original df one type of pointer samj lo point kare 
newdf[0][0]=67856 # setting with copy warning
# print(df)

# newcopy=df.copy() # this is create a copy 
# newcopy[0][0]="copy"
# print(df)

# df.loc[1,1]=133 # loc function

df.columns=list("ABCDE") # change a column
# print(df)

df.loc[2,'C']="ramoliya"
# print(df)

# print(df.drop(9,axis=0)) # drop 9 index row 
# print(df.drop('A',axis=1)) # drop A column 
# print(df.drop(['A','C'],axis=1,inplace=True)) # drop A or C
# ,inplace=True --> aa add karva thi original change tahse
# print(df)

# print(df.loc[[1,2],['A','B']]) # set of row and column

# print(df.loc[:,['A','B']]) # all rows 
# print(df.loc[[1,2],:]) # all column

# print(df.loc[df['A']<0.1])

# print(df.iloc[0,3]) # index se ginti karva mate don't use row and column name

# print(df.iloc[[0,1],[1,2]])

# print(df.reset_index(drop=True)) # ,inplace=True
# print(df)

# w3s=pd.read_csv('w3s.csv')
# print(w3s.dropna())

# print(df['B'].isnull()) # jaya 0 or None hase taya true

# df['B']=None # all B is None but this is not right way use loc

# df.loc[:,['B']]=None
# print(df['B'].isnull())

web = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
                   "toy": [np.nan, np.nan, np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),pd.NaT]})

# print(web.head())
# print(web.dropna()) # all nan is remove

# print(web.dropna(how='all',axis=1)) # If all values are NA, drop that row or column.

# print(web.drop_duplicates(subset=['name'],keep='last'))

# keep=False --> all row is remove
# keep='last' --> last is not remove
# keep='first' --> first is not remove

# print(df.shape)
# print(web.shape)

# print(web.info())
# print(df.info())

# print(web['name'].value_counts(dropna=False))

# print(web.notnull()) 

# 57 min