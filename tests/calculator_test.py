"""Testing the Calculator"""
import pytest
from calculator.main import Calculator
@pytest.fixture
def clear_history():
    """clear history"""
    Calculator.clear_history()
def test_clear_history():
    """test clear history"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count()==0
def get_last_calculation_result():
    """test last calc result"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_result_of_calculation_added_to_history()==4
def get_first_calculation_result():
    """test first calc result"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_result_of_first_calculation_added_to_history()==3
def test_count_history():
    """test count history"""
    assert Calculator.history_count()==0
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.history_count() == 2

