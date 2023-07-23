from typing import List

from ortools.linear_solver import pywraplp

from models.investment_option import investmentOption

class OR_TOOLS_BMCP:
    """
    Class for solving this case as a Budgeted Maximum Conjunction Problem using the OR-Tools library.    
    
    Args:
        investments (List[investmentOption]): A list containing objects of the investmentOption class.
            Each object represents an investment option with its respective attributes.

    Attributes:
        SELECT_HIGH_RISK_MINIMUM (int): The minimum number of high-risk options to be selected.
        SELECT_MEDIUM_RISK_MINIMUM (int): The minimum number of medium-risk options to be selected.
        SELECT_LOW_RISK_MINIMUM (int): The minimum number of low-risk options to be selected.
        COST_HIGH_RISK_THRESHOLD (int): The total cost threshold for high-risk options.
        COST_MEDIUM_RISK_THRESHOLD (int): The total cost threshold for medium-risk options.
        COST_LOW_RISK_THRESHOLD (int): The total cost threshold for low-risk options.
        AVAILABLE_BUDGET (int): The available budget for investment.
        solver: The OR-Tools solver used to solve the optimization problem.

    Methods:
        solve(): Solves the Mixed-Integer Linear Programming (MILP) problem and displays the found solution.
    """

    SELECT_HIGH_RISK_MINIMUM: int = 1
    SELECT_MEDIUM_RISK_MINIMUM: int = 2
    SELECT_LOW_RISK_MINIMUM: int = 2

    COST_HIGH_RISK_THRESHOLD: int = 900000
    COST_MEDIUM_RISK_THRESHOLD: int = 1500000
    COST_LOW_RISK_THRESHOLD: int = 1200000
    
    AVAILABLE_BUDGET: int = 2400000
    
    solver = pywraplp.Solver.CreateSolver("GLOP")


    def solve(self, investments: List[investmentOption]):
        
        if not self.solver:
            return

        for investment in investments:
            print(investment.__str__())            

        decision_binaries = [self.solver.BoolVar(f"option_decision_{i}") for i in range(len(investments))]
        
        objective = self.solver.Objective()

        for option in range(len(investments)):
            objective.SetCoefficient(decision_binaries[option], int(investments[option].payback))
        
        constraint_budget = self.solver.Constraint(-self.solver.infinity(), self.AVAILABLE_BUDGET)

        constraint_low_risk_minimum = self.solver.Constraint(self.SELECT_LOW_RISK_MINIMUM, self.solver.infinity())
        constraint_medium_risk_minimum = self.solver.Constraint(self.SELECT_MEDIUM_RISK_MINIMUM, self.solver.infinity())
        constraint_high_risk_minimum = self.solver.Constraint(self.SELECT_HIGH_RISK_MINIMUM, self.solver.infinity())

        constraint_low_risk_cost = self.solver.Constraint(-self.solver.infinity(), self.COST_LOW_RISK_THRESHOLD)
        constraint_medium_risk_cost = self.solver.Constraint(-self.solver.infinity(), self.COST_MEDIUM_RISK_THRESHOLD)
        constraint_high_risk_cost = self.solver.Constraint(-self.solver.infinity(), self.COST_HIGH_RISK_THRESHOLD)

        for i, investment in enumerate(investments):
            constraint_budget.SetCoefficient(decision_binaries[i], int(investment.cost))
            if investment.risk == 0:
                constraint_low_risk_minimum.SetCoefficient(decision_binaries[i], 1)
                constraint_low_risk_cost.SetCoefficient(decision_binaries[i], int(investment.cost))
            elif investment.risk == 1:
                constraint_medium_risk_minimum.SetCoefficient(decision_binaries[i], 1)
                constraint_medium_risk_cost.SetCoefficient(decision_binaries[i], int(investment.cost))
            elif investment.risk == 2:
                constraint_high_risk_minimum.SetCoefficient(decision_binaries[i], 1)
                constraint_high_risk_cost.SetCoefficient(decision_binaries[i], int(investment.cost))
        
        status = self.solver.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print('Solution:')
            for i, investment in enumerate(investments):
                if decision_binaries[i].solution_value() > 0.99:
                    print(f"Investment option {i}: Cost = {investment.cost}, Payback = {investment.payback}")
            print(f"Total payback: {self.solver.Objective().Value()}")                   
        else:
            print('This case doesnt have a optimal solution.')