import pandas as pd
import numpy as np


##df = pd.read_csv('data.csv')
##
##print df.head()
##
##
##df.columns = ['MatchID', 'Date', 'VS', 'A','B','C','D','E','F', 'G']
##
##print df.head()
##
##df.to_csv('new_data.csv')
##
##df2 = pd.read_csv('new_data.csv', index_col=0)
##
##
##print df2.head()
##
##df2.to_html('new_data.html')

df3 = pd.read_csv('new_data.csv')
df3.to_csv('no_header.csv', header=False)


df4 = pd.read_csv('no_header.csv', names =['ID', 'Date', 'VS', 'A','B','C','D','E','F', 'G'])


arr = np.array(df4[['ID','Date','A']])

df5 = pd.DataFrame(arr)


df5.columns = ['MID','Date','SSS']
df5.to_csv('less.csv')
print df5.head()

df6 = pd.read_csv('less.csv', index_col=0)
df6.set_index('MID', inplace=True)
print df6.head()

df6.to_html('df6.html')
