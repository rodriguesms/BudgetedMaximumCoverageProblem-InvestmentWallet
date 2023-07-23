import unittest

from models.investment_option import investmentOption
from models.optimization.ortools import OR_TOOLS_BMCP

class OR_TOOLS_BMCP_TEST(unittest.TestCase):
    
    def setup(self):
        self.investments = [
            investmentOption(0, "Option 0", 100000, 200000, 0),
            investmentOption(1, "Option 1", 150000, 250000, 1),
            investmentOption(2, "Option 2", 120000, 180000, 0),
        ]

    def solve_test(self):
        self.setup()
        ortools_model = OR_TOOLS_BMCP()
        ortools_model.solve(self.investments)


