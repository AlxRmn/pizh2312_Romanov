import pygame
from settings import CELL_SIZE

class GameObject:
    """
    Базовый класс для игровых объектов (например, змейка и яблоко).

    Атрибуты:
        position (tuple[int, int]): Координаты объекта
        color (tuple[int, int, int]): Цвет объекта
    """

    def __init__(self, position: tuple[int, int], color: tuple[int, int, int]) -> None:
        """
        Инициализирует игровой объект.

        Параметры:
            position (tuple[int, int]): Положение на поле
            color (tuple[int, int, int]): Цвет объекта
        """
        self.position = position
        self.color = color

    def draw(self, screen: pygame.Surface) -> None:
        """
        Отображает объект на экране.

        Параметры:
            screen (pygame.Surface): Поверхность для отрисовки
        """
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))
