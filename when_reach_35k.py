import pandas as pd
import ujson
from collections import defaultdict


df = pd.read_csv("~/Desktop/hk91.csv")


json_str = df.to_json()
json_data = ujson.loads(json_str)

uid_hash = json_data.get("f_uid")
crtime_hash = json_data.get("f_crtime")
money_hash = json_data.get("f_money")


uid_total_money = defaultdict(list)
uid_to_35k_time = {}

for i in range(0, 32110):
    uid = uid_hash.get(str(i))
    money = int(money_hash.get(str(i), 0))
    crtime = crtime_hash.get(str(i))
    uid_total_money[uid].append(money)
    current_sum = sum(uid_total_money.get(uid, 0)) 
    print 'current_sum', current_sum 
    if current_sum > 3500 and uid_to_35k_time.get(uid, -1) == -1:
        uid_to_35k_time[uid] = crtime

print uid_to_35k_time
d = [{"uid":k, "crtime":v} for k, v in uid_to_35k_time.items()]

df2 = pd.read_json(ujson.dumps(d))
df2.to_csv("~/Desktop/uid_to_35k_time.csv")
