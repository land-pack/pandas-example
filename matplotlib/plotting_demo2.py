import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


index = pd.date_range('1/1/2017', periods=1000)

df = pd.DataFrame(np.random.randn(1000, 4), index=index, columns=['A', 'B', 'C', 'D'])


df = df.cumsum()

plt.figure()
plt.plot(df)
plt.legend(loc='best')
plt.savefig('dem2.png')
