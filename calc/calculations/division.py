"""module division"""
from calc.calculations.calculation import Calculation
class Division(Calculation):
    """division"""
    def getresult(self):
        """get result division"""
        return self.value_a / self.value_b
