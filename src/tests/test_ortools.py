import unittest

from models.investment_option import investmentOption
from models.optimization.ortools import OR_TOOLS_BMCP

class OR_TOOLS_BMCP_TEST(unittest.TestCase):
    """
    Class for testing the OR_TOOLS_BMCP class.
    """
    
    def setup(self):
        self.investments = [
            investmentOption(0, "Option 0", 100000, 200000, 0),
            investmentOption(1, "Option 1", 150000, 250000, 1),
            investmentOption(2, "Option 2", 120000, 180000, 0),
            investmentOption(3, "Option 3", 90000, 150000, 1),
            investmentOption(4, "Option 4", 300000, 500000, 2),
            investmentOption(5, "Option 5", 200000, 300000, 2),
        ]
        ortools_model = OR_TOOLS_BMCP()
        ortools_model.solve(self.investments)


    def test_risk_selection(self):
        """
        Test if at least one high-risk investment is selected
        """
        
        self.setup()
        high_risk_selected = any(decision_var.solution_value() > 0.99 for decision_var in self.ortools_model.decision_binaries if self.investments[decision_var.index()].risk == 2)
        self.assertTrue(high_risk_selected, "At least one high-risk investment should be selected")

    def test_medium_risk_selection(self):
        """
        Test if at least two medium-risk investments are selected
        """
        
        self.setup()
        medium_risk_selected_count = sum(decision_var.solution_value() > 0.99 for decision_var in self.ortools_model.decision_binaries if self.investments[decision_var.index()].risk == 1)
        self.assertGreaterEqual(medium_risk_selected_count, 2, "At least two medium-risk investments should be selected")

    def test_low_risk_selection(self):
        """
        Test if at least two low-risk investments are selected
        """

        self.setup()
        low_risk_selected_count = sum(decision_var.solution_value() > 0.99 for decision_var in self.ortools_model.decision_binaries if self.investments[decision_var.index()].risk == 0)
        self.assertGreaterEqual(low_risk_selected_count, 2, "At least two low-risk investments should be selected")

    def test_risk_costs(self):
        """
        Test if the total cost for each risk category is within the threshold
        """

        self.setup()
        total_costs = [sum(decision_var.solution_value() * self.investments[decision_var.index()].cost for decision_var in self.ortools_model.decision_binaries if self.investments[decision_var.index()].risk == risk)
                       for risk in range(3)]  # 3 risk categories: 0 (low), 1 (medium), 2 (high)

        self.assertLessEqual(total_costs[0], 1200000, "Total cost for low-risk investments should be less than or equal to 1200000")
        self.assertLessEqual(total_costs[1], 1500000, "Total cost for medium-risk investments should be less than or equal to 1500000")
        self.assertLessEqual(total_costs[2], 900000, "Total cost for high-risk investments should be less than or equal to 900000")

if __name__ == '__main__':
    unittest.main()
