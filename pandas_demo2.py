import pandas as pd

df = pd.read_csv('ZILL-Z77006_3B.csv')

print(df.head())

df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

#no index column, since date can be index
df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('newcsv3.csv')

#remove columns and save to csv
df.to_csv('newcsv4.csv', header=False)

#adding columns back in
df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)

#pandas to convert data formats
df.to_html('example.html')

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'])
print(df.head())

#remove and rename column
df.rename(columns={'Austin_HPI' : '77006_HPI'}, inplace=True)
print(df.head())


