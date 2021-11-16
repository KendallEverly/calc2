"""module calc"""
from calc.calculation import Calculation
class Addition(Calculation):
    """addition"""
    def getresult(self):
        """get result addition"""
        return self.value_a + self.value_b
