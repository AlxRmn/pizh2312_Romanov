class Ifrit:
    """
    Базовый класс, представляющий Ифрита с атрибутами высоты и имени.
    """
    
    def __init__(self, height: int, name: str):
        """
        Инициализирует Ифрита с высотой и именем.
        
        Назначение:
            Инициализация объекта класса Ifrit.
        
        Параметры:
            height (int): Высота Ифрита.
            name (str): Имя Ифрита.
        
        Результат:
            None.
        """
        self.height = height
        self.name = name
    
class GoodIfrit(Ifrit):
    """
    Класс, представляющий Доброго Ифрита с дополнительным атрибутом доброты.
    Поддерживает арифметические операции, сравнения и возможность вызова как функции.
    """
    
    def __init__(self, height: int, name: str, goodness: int):
        """
        Инициализирует экземпляр с высотой, именем и уровнем доброты.
        
        Назначение:
            Инициализация объекта класса GoodIfrit.
        
        Параметры:
            height (int): Высота Ифрита.
            name (str): Имя Ифрита.
            goodness (int): Уровень доброты Ифрита.
        
        Результат:
            None.
        """
        Ifrit.__init__(self, height, name)
        self.goodness = goodness
    
    def change_goodness(self, value: int):
        """
        Изменяет уровень доброты на указанное значение, не позволяя ему опуститься ниже нуля.
        
        Назначение:
            Изменение значения доброты.
        
        Параметры:
            value (int): Величина, на которую изменяется доброта.
        
        Результат:
            None.
        """
        self.goodness += value
        if self.goodness < 0:
            self.goodness = 0
    
    def __add__(self, number: int) -> 'GoodIfrit':
        """
        Возвращает нового Доброго Ифрита с увеличенной высотой на указанное число.
        
        Назначение:
            Увеличение высоты Ифрита.
        
        Параметры:
            number (int): Величина, на которую увеличивается высота.
        
        Результат:
            GoodIfrit: Новый экземпляр с увеличенной высотой.
        """
        return GoodIfrit(self.height + number, self.name, self.goodness)
    
    def __call__(self, arg: int) -> int:
        """
        Позволяет вызывать экземпляр как функцию, возвращая (arg * доброта) // высота.
        
        Назначение:
            Вызов экземпляра как функции для вычисления выражения.
        
        Параметры:
            arg (int): Число для вычисления с добротой и высотой.
        
        Результат:
            int: Результат выражения (arg * доброта) // высота.
        """
        return (arg * self.goodness) // self.height
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра.
        
        Назначение:
            Представление объекта в виде строки.
        
        Параметры:
            None.
        
        Результат:
            str: Строка, описывающая объект.
        """
        return f"Добрый Ифрит {self.name}, высота {self.height}, доброта {self.goodness}"
    
    def __lt__(self, other: 'GoodIfrit') -> bool:
        """
        Сравнивает экземпляры по уровню доброты, затем по высоте и имени.
        
        Назначение:
            Сравнение двух Ифритов по уровням доброты, высоте и имени.
        
        Параметры:
            other (GoodIfrit): Другой экземпляр для сравнения.
        
        Результат:
            bool: True, если текущий объект меньше другого.
        """
        return (self.goodness, self.height, self.name) < (other.goodness, other.height, other.name)
    
    def __le__(self, other: 'GoodIfrit') -> bool:
        """
        Сравнивает экземпляры по уровню доброты, затем по высоте и имени (меньше или равно).
        
        Назначение:
            Сравнение двух Ифритов по уровням доброты, высоте и имени.
        
        Параметры:
            other (GoodIfrit): Другой экземпляр для сравнения.
        
        Результат:
            bool: True, если текущий объект меньше или равен другому.
        """
        return (self.goodness, self.height, self.name) <= (other.goodness, other.height, other.name)
    
    def __gt__(self, other: 'GoodIfrit') -> bool:
        """
        Сравнивает экземпляры по уровню доброты, затем по высоте и имени (больше).
        
        Назначение:
            Сравнение двух Ифритов по уровням доброты, высоте и имени.
        
        Параметры:
            other (GoodIfrit): Другой экземпляр для сравнения.
        
        Результат:
            bool: True, если текущий объект больше другого.
        """
        return (self.goodness, self.height, self.name) > (other.goodness, other.height, other.name)
    
    def __ge__(self, other: 'GoodIfrit') -> bool:
        """
        Сравнивает экземпляры по уровню доброты, затем по высоте и имени (больше или равно).
        
        Назначение:
            Сравнение двух Ифритов по уровням доброты, высоте и имени.
        
        Параметры:
            other (GoodIfrit): Другой экземпляр для сравнения.
        
        Результат:
            bool: True, если текущий объект больше или равен другому.
        """
        return (self.goodness, self.height, self.name) >= (other.goodness, other.height, other.name)
    
    def __eq__(self, other: 'GoodIfrit') -> bool:
        """
        Сравнивает экземпляры на равенство по доброте, высоте и имени.
        
        Назначение:
            Проверка двух Ифритов на равенство.
        
        Параметры:
            other (GoodIfrit): Другой экземпляр для сравнения.
        
        Результат:
            bool: True, если экземпляры равны.
        """
        return (self.goodness, self.height, self.name) == (other.goodness, other.height, other.name)
    
    def __ne__(self, other: 'GoodIfrit') -> bool:
        """
        Сравнивает экземпляры на неравенство по доброте, высоте и имени.
        
        Назначение:
            Проверка двух Ифритов на неравенство.
        
        Параметры:
            other (GoodIfrit): Другой экземпляр для сравнения.
        
        Результат:
            bool: True, если экземпляры не равны.
        """
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
