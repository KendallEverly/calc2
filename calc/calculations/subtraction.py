"""module subtract"""
from calc.calculations.calculation import Calculation
class Subtraction(Calculation):
    """subtraction"""
    def getresult(self):
        """get the result"""
        return self.value_a - self.value_b
