import pandas as pd
import json
from datetime import datetime, timedelta
from features import tot_claim_cnt_l180d

# load the data in the dataset
df = pd.read_csv("data/data.csv")
contracts = df['contracts']
tot_claim_cnt_l180d(contracts)