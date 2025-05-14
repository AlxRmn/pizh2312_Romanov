import unittest
from unittest.mock import patch

from snake import Snake
from apple import Apple
from settings import CELL_SIZE, WIDTH, HEIGHT, DIRECTIONS

# Константы направлений для тестов
UP: tuple[int, int] = tuple(i * CELL_SIZE for i in DIRECTIONS['UP'])
DOWN: tuple[int, int] = tuple(i * CELL_SIZE for i in DIRECTIONS['DOWN'])
LEFT: tuple[int, int] = tuple(i * CELL_SIZE for i in DIRECTIONS['LEFT'])
RIGHT: tuple[int, int] = tuple(i * CELL_SIZE for i in DIRECTIONS['RIGHT'])


class TestSnakeGame(unittest.TestCase):
    """
    Набор тестов для проверки логики змейки.
    """

    def setUp(self) -> None:
        """
        Инициализация перед каждым тестом: создаётся новая змейка.
        """
        self.snake = Snake()

    def test_snake_initial_position(self) -> None:
        """
        Назначение: Проверяет, что змейка появляется в центре поля.

        Результат:
            координаты головы соответствуют центру экрана.
        """
        expected_position = [(WIDTH // 2, HEIGHT // 2)]
        self.assertEqual(self.snake.body, expected_position)

    def test_snake_moves_correctly(self) -> None:
        """
        Назначение: Проверяет корректность перемещения змейки.

        Результат:
            голова змейки смещается на одну ячейку вправо (по умолчанию).
        """
        initial_pos = self.snake.get_head()
        self.snake.move()
        new_pos = self.snake.get_head()
        expected_pos = ((initial_pos[0] + CELL_SIZE) % WIDTH, initial_pos[1])
        self.assertEqual(new_pos, expected_pos)

    def test_snake_changes_direction(self) -> None:
        """
        Назначение: Проверяет смену направления змейки.

        Результат:
            направление меняется корректно (если не противоположное).
        """
        self.snake.set_direction(UP)
        self.snake.move()
        self.assertEqual(self.snake.direction, UP)

        self.snake.set_direction(LEFT)
        self.snake.move()
        self.assertEqual(self.snake.direction, LEFT)

    def test_snake_does_not_reverse(self) -> None:
        """
        Назначение: Проверяет, что змейка не может развернуться на 180°.

        Результат:
            если направление противоположное — оно игнорируется.
        """
        self.snake.set_direction(LEFT)
        self.snake.move()
        self.assertEqual(self.snake.direction, RIGHT)

        self.snake.set_direction(DOWN)
        self.snake.move()
        self.assertEqual(self.snake.direction, DOWN)

    def test_snake_collides_with_itself(self) -> None:
        """
        Назначение: Проверяет, определяет ли змейка столкновение с собой.

        Результат:
            возвращает True при самопересечении.
        """
        self.snake.body = [(100, 100), (120, 100), (140, 100), (120, 100)]
        self.assertTrue(self.snake.check_self_collision())

    def test_snake_reset(self) -> None:
        """
        Назначение: Проверяет сброс змейки в начальное состояние.

        Результат:
            змейка возвращается в центр и длина = 1.
        """
        self.snake.body = [(40, 40), (60, 40)]
        self.snake.reset()
        self.assertEqual(self.snake.body, [(WIDTH // 2, HEIGHT // 2)])


class TestApple(unittest.TestCase):
    """
    Набор тестов для проверки генерации и логики яблока.
    """

    def setUp(self) -> None:
        """
        Инициализация перед каждым тестом: создаётся новая змейка.
        """
        self.snake = Snake()

    def test_apple_appears_not_on_snake(self) -> None:
        """
        Назначение: Проверяет, что яблоко не создаётся на теле змейки.

        Результат:
            позиция яблока не входит в координаты змейки.
        """
        apple = Apple(self.snake.body)
        self.assertNotIn(apple.position, self.snake.body)

    @patch('random.choice', return_value=(40, 40))
    def test_apple_random_position(self, mock_random: patch) -> None:
        """
        Назначение: Проверяет, что яблоко размещается в заданной ячейке при замоке random.

        Параметры:
            mock_random (patch): фиктивный выбор координат

        Результат:
            яблоко появляется в (40, 40)
        """
        apple = Apple(self.snake.body)
        self.assertEqual(apple.position, (40, 40))


if __name__ == '__main__':
    unittest.main()
