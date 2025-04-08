import pygame
from settings import BLACK, FPS_START, CELL_SIZE, DIRECTIONS, WIDTH, HEIGHT
from snake import Snake
from apple import Apple

class Game:
    """
    Класс, управляющий основным игровым циклом.
    """

    def __init__(self) -> None:
        """
        Инициализация игры.
        """
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Змейка")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps: int = FPS_START

        self.snake = Snake()
        self.apple = Apple(self.snake.body)

    def handle_events(self) -> bool:
        """
        Обрабатывает события (нажатия клавиш, выход).

        Результат:
            bool: True, если игра продолжается
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.fps = max(5, self.fps - 5)
                elif event.key == pygame.K_w:
                    self.fps += 5
                else:
                    self._handle_direction(event.key)

        return True

    def _handle_direction(self, key: int) -> None:
        """
        Обработка смены направления змейки.

        Параметры:
            key (int): код нажатой клавиши
        """
        key_map = {
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN',
            pygame.K_LEFT: 'LEFT',
            pygame.K_RIGHT: 'RIGHT',
        }
        if key in key_map:
            direction = DIRECTIONS[key_map[key]]
            self.snake.set_direction(tuple(i * CELL_SIZE for i in direction))

    def update(self) -> None:
        """
        Обновляет состояние игры (движение, столкновения).
        """
        self.snake.move()

        if self.snake.get_head() == self.apple.position:
            self.apple.relocate(self.snake.body)
        else:
            self.snake.trim_tail()

        if self.snake.check_self_collision():
            self.snake.reset()
            self.apple.relocate(self.snake.body)

    def render(self) -> None:
        """
        Отрисовывает всё на экране.
        """
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        """
        Запускает основной цикл игры.
        """
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

        pygame.quit()
