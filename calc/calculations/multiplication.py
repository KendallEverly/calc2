"""module multiply"""
from calc.calculations.calculation import Calculation
class Multiplication(Calculation):
    """multiplication"""
    def getresult(self):
        """get the result"""
        return self.value_a * self.value_b
