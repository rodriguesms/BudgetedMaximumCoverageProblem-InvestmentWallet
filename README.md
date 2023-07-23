# Investment Selection with OR-Tools

This challenge development was based on the Budgeted Maximum Coverage Problem.

## Overview

This repository contains a Python program that solves the Investment Selection Problem using Mixed-Integer Linear Programming (MILP) with OR-Tools. The program selects the best investment options based on risk categories, budget constraints, and expected payback values.

## Requirements

To run the program, you need the following:

- Python (3.x)
- OR-Tools (installation instructions can be found [here](https://developers.google.com/optimization/install))

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/rodriguesms/BudgetedMaximumCoverageProblem-InvestmentWallet.git
   cd BudgetedMaximumCoverageProblem-InvestmentWallet
   ```
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Run the program:

    ```bash
    python src/main.py
    ```

The program will display the selected investment options and their total payback.