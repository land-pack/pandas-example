import pandas as pd
import numpy as np
from pyecharts import Bar
from pyecharts.base import Base

index = pd.date_range('3/8/2017', periods=6, freq='M')
df1 = pd.DataFrame(np.random.randn(6), index=index)
dtvalue1, pdattr1 = Base.pdcast(df1)

df2 = pd.DataFrame(np.random.randn(6), index=index)
dtvalue2, pdattr2 = Base.pdcast(df2)

dtvalue1 = [i[0] for i in dtvalue1]
dtvalue2 = [i[0] for i in dtvalue2]

bar = Bar('MyBar', 'precipitation and evaporation one year')
bar.add('precipitation', pdattr1,  dtvalue1, mark_line=['average'], mark_point=['max', 'min'])
bar.add('evaporation', pdattr2,  dtvalue2, mark_line=['average'], mark_point=['max', 'min'])
bar.render()
