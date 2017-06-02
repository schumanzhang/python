import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#dataframe is like a python dictonary
web_stats = {'Day' : [1, 2, 3, 4, 5, 6],
            'Visitors' : [34, 56, 34, 56, 23, 56],
            'Bounce_Rate' : [65, 74, 23, 88, 93, 67]}

#how to convert above to a dataframe?
df = pd.DataFrame(web_stats)

#print(df)
#print first 5 rows
print(df.head())

#print the last 5 rows
print(df.tail())

#print the last 2 rows
print(df.tail(2))

#look at index, time series data, index should be Day
#the following returns a new dataframe, second line modifies the dataframe
df.set_index('Day')
df.set_index('Day', inplace=True)
print(df.head())

#reference a column
print(df['Visitors'])
print(df.Visitors)

#show two columns
print(df[['Bounce_Rate', 'Visitors']])

#convert a column to a list
print(df.Visitors.tolist())
#use numpy to convert to a numpy array
print(np.array(df[['Bounce_Rate', 'Visitors']]))

#create new dataframe
df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))

print(df2)