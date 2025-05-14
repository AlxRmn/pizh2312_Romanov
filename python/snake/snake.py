import pygame
from settings import WIDTH, HEIGHT, CELL_SIZE, GREEN

class Snake:
    """
    Класс, представляющий змейку игрока.
    """

    def __init__(self) -> None:
        """
        Создаёт змейку в центре поля.
        """
        center = (WIDTH // 2, HEIGHT // 2)
        self.body: list[tuple[int, int]] = [center]
        self.color: tuple[int, int, int] = GREEN
        self.direction: tuple[int, int] = (CELL_SIZE, 0)
        self.next_direction: tuple[int, int] = self.direction

    def move(self) -> None:
        """
        Передвигает змейку в текущем направлении.
        """
        if self._valid_direction_change():
            self.direction = self.next_direction

        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % WIDTH, (head_y + dy) % HEIGHT)
        self.body.insert(0, new_head)

    def trim_tail(self) -> None:
        """
        Удаляет последний сегмент (если не съедено яблоко).
        """
        self.body.pop()

    def grow(self) -> None:
        """
        Змейка увеличивается — ничего не удаляется.
        """
        pass

    def check_self_collision(self) -> bool:
        """
        Проверяет, столкнулась ли змейка сама с собой.

        Результат:
            bool: True, если произошло столкновение
        """
        return len(self.body) != len(set(self.body))

    def reset(self) -> None:
        """
        Сброс состояния змейки.
        """
        self.__init__()

    def set_direction(self, new_dir: tuple[int, int]) -> None:
        """
        Задаёт новое направление движения.

        Параметры:
            new_dir (tuple[int, int]): Направление
        """
        self.next_direction = new_dir

    def _valid_direction_change(self) -> bool:
        """
        Проверяет, допустима ли смена направления (не в противоположную сторону).

        Результат:
            bool: True, если направление корректно
        """
        dx1, dy1 = self.direction
        dx2, dy2 = self.next_direction
        return (dx1 + dx2, dy1 + dy2) != (0, 0)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Отрисовывает змейку.

        Параметры:
            screen (pygame.Surface): Поверхность
        """
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (*segment, CELL_SIZE, CELL_SIZE))

    def get_head(self) -> tuple[int, int]:
        """
        Возвращает позицию головы змейки.

        Результат:
            tuple[int, int]: координаты головы
        """
        return self.body[0]
