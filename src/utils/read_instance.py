from typing import List

from models.investment_option import investmentOption

from utils.risk_mapping import risk_mapping

import csv

def read_csv(filepath: str) -> List[investmentOption]:
    investment_options: List[investmentOption] = []
    
    with open(file=filepath, newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            option, description, cost, payback, risk = row
            investment_options.append(investmentOption(option, description, cost, payback, risk_mapping(risk)))

    return investment_options