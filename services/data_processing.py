import pandas as pd
from features import tot_claim_cnt_l180d, disb_bank_loan_wo_tbc, day_sinlastloan

def process_data(input_file, output_file):
    # open csv, apply features, save and return results.
    df = pd.read_csv(input_file)

    # Apply feature functions
    df["tot_claim_cnt_l180d"] = df["contracts"].apply(tot_claim_cnt_l180d)
    df["disb_bank_loan_wo_tbc"] = df["contracts"].apply(disb_bank_loan_wo_tbc)
    df["day_sinlastloan"] = df["contracts"].apply(day_sinlastloan)

    # Save processed data
    df.to_csv(output_file, index=False)

    return df
