import pandas as pd
import numpy as np


web_status = {
    "Day": [ 1, 2, 3, 4, 5, 6],
    "Visitors": [56, 33, 223, 56, 142, 229],
    "Bar_tag": [245, 345, 334, 566, 432, 444]
}

df = pd.DataFrame(web_status)

#print df
#
#print df.head(3)
#
#print df.tail(2)
#
#print df.set_index('Day')
#
#
#print df
#
#
#print df.set_index('Day', inplace=True)
#
#print df



print df.Day
print df[['Day', 'Visitors']]
print df.Day.tolist()



web_status2 = np.array(df[['Day', 'Visitors']])
print web_status2


#
