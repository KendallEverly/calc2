"""Testing the Calculator"""
import pprint

import pytest

from calculator.main import Calculator
@pytest.fixture
def clear_history():
    Calculator.clear_history()
def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    #Assert that the results are correct
    assert Calculator.add_number(1,2)==3
    assert Calculator.add_number(2,2)==4
    assert Calculator.history_count()==2
    assert Calculator.get_result_of_calculation_added_to_history()==4
    pprint.pp(Calculator.history)
def test_clear_history(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.history_count() == 2
    assert Calculator.clear_history()==True
    assert Calculator.history_count()==0
def get_last_calculation_result(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_result_of_calculation_added_to_history()==4
def get_first_calculation_result(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_result_of_first_calculation_added_to_history()==3
def test_count_history(clear_history):
    assert Calculator.history_count()==0
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.history_count() == 2
def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1,2)==-1
def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2)==2
def test_calculator_divide(clear_history):
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(1,2)==0.5
