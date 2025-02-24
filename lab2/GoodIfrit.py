class Ifrit:
    """Базовый класс, представляющий Ифрита с атрибутами высоты и имени."""
    
    def __init__(self, height, name):
        """Инициализирует Ифрита с высотой и именем."""
        self.height = height
        self.name = name
    
class GoodIfrit(Ifrit):
    """Класс, представляющий Доброго Ифрита с дополнительным атрибутом доброты.
    Поддерживает арифметические операции, сравнения и возможность вызова как функции."""
    
    def __init__(self, height, name, goodness):
        """Инициализирует экземпляр с высотой, именем и уровнем доброты."""
        Ifrit.__init__(self, height, name)
        self.goodness = goodness
    
    def change_goodness(self, value):
        """Изменяет уровень доброты на указанное значение, не позволяя ему опуститься ниже нуля."""
        self.goodness += value
        if (self.goodness < 0):
            self.goodness = 0
    
    def __add__(self, number):
        """Возвращает нового Доброго Ифрита с увеличенной высотой на указанное число."""
        return GoodIfrit(self.height + number, self.name, self.goodness)
    
    def __call__(self, arg):
        """Позволяет вызывать экземпляр как функцию, возвращая (arg * доброта) // высота."""
        return (arg * self.goodness) // self.height
    
    def __str__(self):
        """Возвращает строковое представление экземпляра."""
        return f"Добрый Ифрит {self.name}, высота {self.height}, доброта {self.goodness}"
    
    def __lt__(self, other):
        """Сравнивает экземпляры по уровню доброты, затем по высоте и имени."""
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
