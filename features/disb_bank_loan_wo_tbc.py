import json
import math

def disb_bank_loan_wo_tbc(contracts):
    try:
        if isinstance(contracts, str):
            contracts = json.loads(contracts)
        elif isinstance(contracts, float):
            return -1
        if isinstance(contracts, dict):
            contracts = [contracts]
        result = 0
        for contract in contracts:
            bank = contract.get("bank")
            contract_date = contract.get("contract_date")
            loan_summa = contract.get("loan_summa", 0)
            if bank not in ['LIZ', 'LOM', 'MKO', 'SUG', "", None] and contract_date not in [None,  ""] and loan_summa != "":
                result += contract.get("loan_summa", 0)
        if result == 0:
            return -3
        else:
            return result
    except Exception as e:
        print('Error: ', e)
