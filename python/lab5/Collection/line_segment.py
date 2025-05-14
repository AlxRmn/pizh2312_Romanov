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

    def to_dict(self) -> dict:
        """
        Преобразует объект в словарь.

        Результат:
        dict: Словарь с координатами.
        """
        return {"x1": self.x1, "y1": self.y1, "x2": self.x2, "y2": self.y2}

    @classmethod
    def from_dict(cls, data: dict) -> "LineSegment":
        """
        Создает объект LineSegment из словаря.

        Параметры:
        data (dict): Словарь с координатами.

        Результат:
        LineSegment: Объект класса.
        """
        return cls(data["x1"], data["y1"], data["x2"], data["y2"])
