import pandas as pd
from features import tot_claim_cnt_l180d, disb_bank_loan_wo_tbc, day_sinlastloan

# load the data in the dataset
df = pd.read_csv("data/data.csv")
contracts = df['contracts']

df['tot_claim_cnt_l180d'] = df['contracts'].apply(tot_claim_cnt_l180d)
df['disb_bank_loan_wo_tbc'] = df['contracts'].apply(disb_bank_loan_wo_tbc)
df['day_sinlastloan'] = df['contracts'].apply(day_sinlastloan)
# print(df['tot_claim_cnt_l180d'])
print(df['day_sinlastloan'])
# print(df['disb_bank_loan_wo_tbc'])
