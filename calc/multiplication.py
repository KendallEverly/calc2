"""module multiply"""
from calc.calculation import Calculation
class Multiplication(Calculation):
    """multiplication"""
    def getresult(self):
        """get the result"""
        return self.value_a * self.value_b
