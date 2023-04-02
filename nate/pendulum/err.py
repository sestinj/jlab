import numpy as np

class Measurement:
    """Where error is defined as standard deviation divided by mean."""
    def __init__(self, value, error):
        self.value = value
        self.error = error

    @classmethod
    def from_list(cls, values):
        return cls(np.mean(values), np.std(values) / np.mean(values))
    
    def __add__(self, other):
        return Measurement(self.value + other.value, self.error + other.error)
    
    def __sub__(self, other):
        return Measurement(self.value - other.value, self.error + other.error)
    
    def __mul__(self, other):
        if isinstance(other, Measurement):
            return Measurement(self.value * other.value, np.sqrt(self.error**2 + other.error**2))
        else:
            return Measurement(self.value * other, self.error)
    
    def __rmul__(self, other):
        if isinstance(other, Measurement):
            return Measurement(self.value * other.value, np.sqrt(self.error**2 + other.error**2))
        else:
            return Measurement(self.value * other, self.error)
    
    def __truediv__(self, other):
        if isinstance(other, Measurement):
            return Measurement(self.value / other.value, np.sqrt(self.error**2 + other.error**2))
        else:
            return Measurement(self.value / other, self.error)
        
    def __rtruediv__(self, other):
        if isinstance(other, Measurement):
            return Measurement(other.value / self.value, np.sqrt(self.error**2 + other.error**2))
        else:
            return Measurement(other / self.value, self.error)
    
    def __pow__(self, other):
        return Measurement(self.value ** other, other * self.error)
    
    def __repr__(self):
        return f"{self.value:.3f}\u00B1{self.error:.3f}"