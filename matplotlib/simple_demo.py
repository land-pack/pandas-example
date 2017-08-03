import pandas as pd
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt
ts = pd.Series(random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
