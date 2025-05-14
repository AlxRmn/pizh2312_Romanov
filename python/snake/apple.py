import random
from game_object import GameObject
from settings import RED, WIDTH, HEIGHT, CELL_SIZE

class Apple(GameObject):
    """
    Класс, представляющий яблоко, которое должна съесть змейка.
    """

    def __init__(self, snake_positions: list[tuple[int, int]]) -> None:
        """
        Инициализирует объект яблока и размещает его на свободной ячейке.

        Параметры:
            snake_positions (list[tuple[int, int]]): Ячейки, занятые змейкой
        """
        self.all_cells = [
            (x * CELL_SIZE, y * CELL_SIZE)
            for x in range(WIDTH // CELL_SIZE)
            for y in range(HEIGHT // CELL_SIZE)
        ]
        super().__init__((0, 0), RED)
        self.relocate(snake_positions)

    def relocate(self, snake_positions: list[tuple[int, int]]) -> None:
        """
        Размещает яблоко на случайной свободной клетке.

        Параметры:
            snake_positions (list[tuple[int, int]]): Ячейки, занятые змейкой
        """
        free_cells = list(set(self.all_cells) - set(snake_positions))
        if not free_cells:
            raise Exception("Нет свободных ячеек!")
        self.position = random.choice(free_cells)
