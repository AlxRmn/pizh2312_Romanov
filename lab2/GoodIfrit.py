class Ifrit:
    """
    Base class representing a generic Ifrit with height and name attributes.
    """
    
    def __init__(self, height, name):
        """Initialize an Ifrit with height and name."""
        self.height = height
        self.name = name
    
class GoodIfrit(Ifrit):
    """
    A class representing a Good Ifrit with an additional goodness attribute.
    Supports arithmetic operations, comparisons, and callable behavior.
    """
    
    def __init__(self, height, name, goodness):
        """Initialize an instance with height, name, and goodness."""
        Ifrit.__init__(self, height, name)
        self.goodness = goodness
    
    def change_goodness(self, value):
        """Modify goodness by a given value, ensuring it does not go below zero."""
        self.goodness += value
        if self.goodness < 0:
            self.goodness = 0
    
    def __add__(self, number):
        """Return a new GoodIfrit with increased height by the given number."""
        return GoodIfrit(self.height + number, self.name, self.goodness)
    
    def __call__(self, arg):
        """Enable the instance to be called as a function, returning (arg * goodness) // height."""
        return (arg * self.goodness) // self.height
    
    def __str__(self):
        """Return a string representation of the instance."""
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"
    
    def __lt__(self, other):
        """Compare instances based on goodness, then height, then name."""
        return (self.goodness, self.height, self.name) < (other.goodness, other.height, other.name)
    
    def __le__(self, other):
        return (self.goodness, self.height, self.name) <= (other.goodness, other.height, other.name)
    
    def __gt__(self, other):
        return (self.goodness, self.height, self.name) > (other.goodness, other.height, other.name)
    
    def __ge__(self, other):
        return (self.goodness, self.height, self.name) >= (other.goodness, other.height, other.name)
    
    def __eq__(self, other):
        return (self.goodness, self.height, self.name) == (other.goodness, other.height, other.name)
    
    def __ne__(self, other):
        return (self.goodness, self.height, self.name) != (other.goodness, other.height, other.name)

# 1

gi = GoodIfrit(80, "Hazrul", 3)  
gi.change_goodness(4)  
print(gi)  
gi1 = gi + 15  
print(gi1)  
print(gi(31))  

# 2

gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)
gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1, sep='\n')
