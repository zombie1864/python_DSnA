import pytest
from module_one._04_savings import SavingsCalculator


def test_savings_calculator_case_1(): 

    savings = SavingsCalculator(120000, 500000, 0.03)
    assert savings.months(.05) == 142


def test_savings_calculator_case_2(): 

    savings = SavingsCalculator(80000, 800000, 0.03)
    assert savings.months(.1) == 159 


def test_savings_calculator_case_3(): 

    savings = SavingsCalculator(75000, 1500000, .05)
    assert savings.months(.05) == 261
