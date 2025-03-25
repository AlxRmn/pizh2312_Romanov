class WritingTool:
    """
    Базовый класс для пишущих принадлежностей.
    """

    def __init__(self, brand: str) -> None:
        """
        Инициализация пишущего инструмента.

        Параметры:
        brand (str): Бренд инструмента.
        """
        self.brand = brand

    def write(self, text: str) -> None:
        """
        Метод для написания текста.

        Параметры:
        text (str): Текст, который нужно написать.
        """
        print(f"{self.brand} пишет: {text}")


class Pencil(WritingTool):
    """
    Класс для карандаша.
    """
    def __init__(self, brand: str, hardness: str) -> None:
        """
        Инициализация карандаша.

        Параметры:
        brand (str): Бренд карандаша.
        hardness (str): Твердость грифеля.
        """
        super().__init__(brand)
        self.hardness = hardness


class Pen(WritingTool):
    """
    Класс для ручки.
    """
    def __init__(self, brand: str, ink_color: str) -> None:
        """
        Инициализация ручки.

        Параметры:
        brand (str): Бренд ручки.
        ink_color (str): Цвет чернил.
        """
        super().__init__(brand)
        self.ink_color = ink_color


class GelPen(Pen):
    """
    Класс для гелевой ручки.
    """
    def __init__(self, brand: str, ink_color: str, tip_size: float) -> None:
        """
        Инициализация гелевой ручки.

        Параметры:
        brand (str): Бренд ручки.
        ink_color (str): Цвет чернил.
        tip_size (float): Толщина наконечника.
        """
        super().__init__(brand, ink_color)
        self.tip_size = tip_size
