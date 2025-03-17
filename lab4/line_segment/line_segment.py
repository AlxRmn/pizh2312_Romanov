import json
from math import sqrt

class LineSegment:
    """
    Класс, представляющий математический отрезок на плоскости.
    """
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        Инициализация отрезка по координатам двух точек.
        
        Параметры:
        x1, y1 (float): Координаты первой точки.
        x2, y2 (float): Координаты второй точки.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление отрезка.
        
        Результат:
        str: Строка с координатами.
        """
        return f"LineSegment(({self.x1}, {self.y1}) - ({self.x2}, {self.y2}))"
    
    def length(self) -> float:
        """
        Вычисляет длину отрезка.
        
        Результат:
        float: Длина отрезка.
        """
        return sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
    
    def save(self, filename: str) -> None:
        """
        Сохраняет объект в JSON-файл.
        
        Параметры:
        filename (str): Имя файла для сохранения.
        """
        with open(filename, "w") as file:
            json.dump(self.__dict__, file)
    
    @classmethod
    def load(cls, filename: str):
        """
        Загружает объект из JSON-файла.
        
        Параметры:
        filename (str): Имя файла для загрузки.
        
        Результат:
        LineSegment: Восстановленный объект класса.
        """
        with open(filename, "r") as file:
            data = json.load(file)
        return cls(data["x1"], data["y1"], data["x2"], data["y2"])
    
    @classmethod
    def from_string(cls, str_value: str):
        """
        Создает объект из строки формата "x1,y1,x2,y2".
        
        Параметры:
        str_value (str): Строка с координатами.
        
        Результат:
        LineSegment: Созданный объект.
        """
        x1, y1, x2, y2 = map(float, str_value.split(","))
        return cls(x1, y1, x2, y2)