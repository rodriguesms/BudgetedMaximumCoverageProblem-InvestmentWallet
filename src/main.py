from utils.read_instance import read_csv

from typing import List

from models.investment_option import investmentOption
from models.optimization.ortools import OR_TOOLS_BMCP

# The Budgeted Maximum Coverage Problem

investments: List[investmentOption] = read_csv('data/OTM Enacom.csv')

ortools_model = OR_TOOLS_BMCP()

ortools_model.solve(investments)