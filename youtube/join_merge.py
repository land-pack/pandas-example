import pandas as pd


example1 = {
        "name": ['frank', 'jack', 'li','ss'],
        'age': [25, 23, 21, 8],
        "Index": [1, 2, 3, 5]
}

example2 = {
        'score': [215, 213, 221, 88],
        "Index": [1, 2, 3, 4]
}


df1 = pd.DataFrame(example1)

df2 = pd.DataFrame(example2)



#df3 = pd.merge(df1, df2, on='Index', how='outer')
#df3 = pd.merge(df1, df2, on='Index', how='inner')
#df3 = pd.merge(df1, df2, on='Index', how='left')
df3 = pd.merge(df1, df2, on='Index', how='right')
df3.set_index('Index', inplace=True)
print df3
