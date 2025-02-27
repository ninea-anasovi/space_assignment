import json
from datetime import datetime, timedelta

def tot_claim_cnt_l180d(contracts):
    try:
        if isinstance(contracts, str):
            contracts = json.loads(contracts)
        elif isinstance(contracts, float):
            return -3
        if isinstance(contracts, dict):
            contracts = [contracts]
        l180d_date = datetime.now() - timedelta(days=180)
        result = 0
        for contract in contracts:
            claim_date_str = contract.get("claim_date", "01.01.1900")
            try:
                claim_date = datetime.strptime(claim_date_str, "%d.%m.%Y")
                if claim_date >= l180d_date:
                    result += 1
            except ValueError:
                continue
        return result
    except Exception as e:
        print('Error: ', e)