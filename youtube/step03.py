# How to concat a dataframe
# How to append a Series to a dataframe


import pandas as pd



example = {
            "HPI": [23, 33, 55, 221, 84],
            "Rate": [34, 224, 98, 223, 23],
}

df1 = pd.DataFrame(example, index=[2013, 2014, 2015, 2016, 2017])

print df1.head()

    
example2 = {
            "HPI": [213, 323, 535, 4221, 384],
            "Rate": [344, 6224, 698, 5223, 223],
}

df2 = pd.DataFrame(example2, index=[2003, 2004, 2005, 2006, 2007])


print pd.concat([df1, df2])



s = pd.Series([22, 224], index= ['HPI', 'Rate'])

print df2.head()

print df2.append(s, ignore_index=True)
