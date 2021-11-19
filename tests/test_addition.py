"""Addition Class"""
from calc.calculations.calculation import Calculation
from calculator.main import Calculator
import pprint
class Addition(Calculation):
    """ calculation addition class"""
def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2)==3
    assert Calculator.add_number(2,2)==4
    assert Calculator.history_count()==2
    assert Calculator.get_result_of_calculation_added_to_history()==4
    pprint.pp(Calculator.history)