"""Multiplication Class"""
from calc.calculations.calculation import Calculation
from calculator.main import Calculator
class Multiplication(Calculation):
    """multiplication calculation object"""
    def test_calculator_multiply(self):
        """ tests multiplication of two numbers"""
        assert Calculator.multiply_numbers(1, 2) == 2