class GoodIfrit:

    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = goodness
    
    def change_goodness(self, value):
        self.goodness += value
        if self.goodness < 0:
            self.goodness = 0
    
    def __add__(self, number):
        return GoodIfrit(self.height + number, self.name, self.goodness)
    
    def __call__(self, arg):
        return (arg * self.goodness) // self.height
    
    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"

    def __lt__(self, other):
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
