import json
from datetime import datetime

def day_sinlastloan(contracts):
    try:
        if isinstance(contracts, str):
            contracts = json.loads(contracts)
        elif isinstance(contracts, float):
            return -1
        if isinstance(contracts, dict):
            contracts = [contracts]
        valid_loans = [
            contract for contract in contracts
            if not contract.get("summa") in [None, ""]
        ]
        if not valid_loans:
            return -3
        last_loan = max(valid_loans, key=lambda x: datetime.strptime(x.get("contract_date", "01.01.1900"), "%d.%m.%Y"))
        contract_date = datetime.strptime(last_loan["contract_date"], "%d.%m.%Y")
        today_date = datetime.now()
        return (today_date - contract_date).days
    except Exception as e:
        print('Error: ', e)
