"""module division"""
from calc.calculation import Calculation
class Division(Calculation):
    """division"""
    def getresult(self):
        """get result division"""
        return self.value_a / self.value_b
