"""Subtraction Class"""
from calc.calculations.calculation import Calculation
from calculator.main import Calculator
class Subtraction(Calculation):
    """subtraction calculation object"""
    def test_calculator_subtract(self):
        """Testing the subtract method of the calculator"""
        assert Calculator.subtract_number(1, 2) == -1
        assert Calculator.subtract_number(2, 2) == 0
