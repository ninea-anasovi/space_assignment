import pandas as pd
import json
from datetime import datetime, timedelta
from features import tot_claim_cnt_l180d

# load the data in the dataset
df = pd.read_csv("data/data.csv")
contracts = df['contracts']

df['tot_claim_cnt_l180d'] = df['contracts'].apply(tot_claim_cnt_l180d)

# contracts = json.loads(contracts)
#
# datetime.strptime(contracts[0].get("claim_date", "1900-01-01"), "%Y-%m-%d")
print(df['tot_claim_cnt_l180d'])