"""Division Class"""
from calc.calculations.calculation import Calculation
from calculator.main import Calculator
class Divide(Calculation):
    """multiplication calculation object"""
def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(1,2)==0.5