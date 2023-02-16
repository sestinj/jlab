class Measurement:
    val: float
    var: float

    def __init__(self, val: float, var: float):
        self.val = val
        self.var = var

    def __add__(self, other):
        return Measurement(self.val + other.val, self.var + other.var)
    
    def __sub__(self, other):
        return Measurement(self.val - other.val, self.var + other.var)
    
    def __mul__(self, other):
        out = self.val * other.val
        return Measurement(out, out**2 * (self.var / self.val**2 + other.var / other.val**2))
    
    def __truediv__(self, other):
        return self * Measurement(1 / other.val, other.var / other.val**2)