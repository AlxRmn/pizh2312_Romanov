class Pizza:
    """
    Класс, представляющий пиццу.

    Атрибуты:
        name (str): Название пиццы.
        dough (str): Тип теста для пиццы.
        sauce (str): Тип соуса, используемого для пиццы.
        toppings (list): Список ингредиентов (начинок) на пицце.
        price (float): Цена пиццы.
    """
    def __init__(self, name: str, dough: str, sauce: str, toppings: list, price: float):
        """
        Инициализирует объект пиццы.

        Параметры:
            name (str): Название пиццы.
            dough (str): Тип теста.
            sauce (str): Тип соуса.
            toppings (list): Список начинок на пицце.
            price (float): Цена пиццы.
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление пиццы.

        Результат:
            str: Строка с названием пиццы и ее ценой.
        """
        return f"{self.name}: {self.price} руб."

    def prepare(self) -> None:
        """
        Подготавливает пиццу (замешивает тесто, собирает ингредиенты и т.д.).

        Результат:
            None
        """
        print(f"Готовим пиццу {self.name}...")

    def bake(self) -> None:
        """
        Выпекает пиццу.

        Результат:
            None
        """
        print(f"Выпекаем пиццу {self.name}...")

    def slice(self) -> None:
        """
        Режет пиццу.

        Результат:
            None
        """
        print(f"Режем пиццу {self.name}...")

    def pack(self) -> None:
        """
        Упаковывает пиццу для доставки.

        Результат:
            None
        """
        print(f"Упаковываем пиццу {self.name}...")


class PepperoniPizza(Pizza):
    """
    Конкретный тип пиццы: Пепперони.
    Наследуется от класса Pizza с предустановленными характеристиками пиццы Пепперони.
    """
    def __init__(self):
        """
        Инициализирует пиццу Пепперони с предустановленными характеристиками.

        Параметры:
            None
        """
        super().__init__("Пепперони", "тонкое", "томатный", ["пепперони", "сыр"], 10)


class BBQPizza(Pizza):
    """
    Конкретный тип пиццы: Барбекю.
    Наследуется от класса Pizza с предустановленными характеристиками пиццы Барбекю.
    """
    def __init__(self):
        """
        Инициализирует пиццу Барбекю с предустановленными характеристиками.

        Параметры:
            None
        """
        super().__init__("Барбекю", "традиционное", "барбекю", ["курица", "лук", "сыр"], 12)


class SeafoodPizza(Pizza):
    """
    Конкретный тип пиццы: Дары Моря.
    Наследуется от класса Pizza с предустановленными характеристиками пиццы Дары Моря.
    """
    def __init__(self):
        """
        Инициализирует пиццу Дары Моря с предустановленными характеристиками.

        Параметры:
            None
        """
        super().__init__("Дары Моря", "тонкое", "сливочный", ["креветки", "мидии", "сыр"], 14)


class Order:
    """
    Класс, представляющий заказ.

    Атрибуты:
        order_counter (int): Счётчик для подсчёта количества заказов.
        number (int): Уникальный номер заказа.
        ordered_pizzas (list): Список заказанных пицц.
    """
    order_counter = 0

    def __init__(self):
        """
        Инициализирует объект заказа.

        Параметры:
            None
        """
        Order.order_counter += 1
        self.number = Order.order_counter
        self.ordered_pizzas = []

    def add(self, pizza: Pizza) -> None:
        """
        Добавляет пиццу в заказ.

        Параметры:
            pizza (Pizza): Объект пиццы, который добавляется в заказ.

        Результат:
            None
        """
        self.ordered_pizzas.append(pizza)

    def total(self) -> float:
        """
        Вычисляет общую стоимость заказа.

        Результат:
            float: Общая стоимость всех пицц в заказе.
        """
        return sum(pizza.price for pizza in self.ordered_pizzas)

    def process(self) -> None:
        """
        Обрабатывает заказ: готовит, выпекает, режет и упаковывает все пиццы.

        Результат:
            None
        """
        print(f"Заказ #{self.number} выполняется...")
        for pizza in self.ordered_pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.slice()
            pizza.pack()
        print(f"Заказ #{self.number} готов!")


class Terminal:
    """
    Класс, представляющий терминал, который взаимодействует с пользователем.

    Атрибуты:
        menu (list): Список доступных пицц.
        order (Order): Текущий заказ, который обрабатывается.
        display_menu (bool): Переменная, указывающая, нужно ли отображать меню.
    """
    def __init__(self):
        """
        Инициализирует объект терминала.

        Параметры:
            None
        """
        self.menu = [PepperoniPizza(), BBQPizza(), SeafoodPizza()]
        self.order = None
        self.display_menu = True

    def show_menu(self) -> None:
        """
        Отображает меню доступных пицц.

        Результат:
            None
        """
        print("Меню:")
        for i, pizza in enumerate(self.menu, 1):
            print(f"{i}. {pizza}")

    def process_command(self, command: str) -> None:
        """
        Обрабатывает команду пользователя.

        Параметры:
            command (str): Команда для обработки (например, "new", "1", "confirm", "payment").

        Результат:
            None
        """
        if command == "new":
            self.order = Order()
            print("Создан новый заказ.")
        elif command.isdigit():
            index = int(command) - 1
            if 0 <= index < len(self.menu):
                pizza = self.menu[index]
                self.order.add(pizza)
                print(f"Добавлена {pizza.name}.")
        elif command == "confirm":
            print(f"Заказ подтвержден. Общая сумма: {self.order.total()} руб.")
        elif command == "payment":
            print("Оплата принята. Заказ отправлен на выполнение.")
            self.order.process()


# Пример работы терминала
terminal = Terminal()
terminal.show_menu()
terminal.process_command("new")
terminal.process_command("1")
terminal.process_command("2")
terminal.process_command("confirm")
terminal.process_command("payment")
