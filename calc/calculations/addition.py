"""module calc"""
from calc.calculations.calculation import Calculation
class Addition(Calculation):
    """addition"""
    def getresult(self):
        """get result addition"""
        return self.value_a + self.value_b
