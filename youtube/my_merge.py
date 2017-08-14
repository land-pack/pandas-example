import pandas as pd

history_recharge = {
    "uid": [1002922, 1002923, 1002924],
    "money": [120, 230, 220]
}

current_recharge = {
    "uid": [1002922, 1002925, 1002926],
    "money": [230, 330, 210]
}


df1 = pd.DataFrame(history_recharge)
df2 = pd.DataFrame(current_recharge)




df3 =  df2[~df2.isin(df1.uid)['uid']]


if __name__ == '__main__':
    print df3
