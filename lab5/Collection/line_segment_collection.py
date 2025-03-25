import json
from line_segment import LineSegment

class LineSegmentCollection:
    """
    Класс-контейнер для хранения и управления объектами LineSegment.
    """

    def __init__(self) -> None:
        """
        Инициализация пустой коллекции отрезков.
        """
        self._data: list[LineSegment] = []

    def __str__(self) -> str:
        """
        Возвращает строковое представление контейнера.

        Результат:
        str: Строковое представление коллекции.
        """
        return f"LineSegmentCollection({self._data})"

    def __getitem__(self, index: int) -> LineSegment:
        """
        Позволяет получать элемент коллекции по индексу.

        Параметры:
        index (int): Индекс элемента.

        Результат:
        LineSegment: Объект класса LineSegment.
        """
        return self._data[index]

    def add(self, segment: LineSegment) -> None:
        """
        Добавляет объект LineSegment в коллекцию.

        Параметры:
        segment (LineSegment): Объект для добавления.
        """
        if isinstance(segment, LineSegment):
            self._data.append(segment)
        else:
            raise TypeError("Можно добавлять только объекты класса LineSegment")

    def remove(self, index: int) -> None:
        """
        Удаляет элемент по индексу.

        Параметры:
        index (int): Индекс удаляемого элемента.

        Результат:
        None
        """
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Индекс вне диапазона")

    def save(self, filename: str) -> None:
        """
        Сохраняет коллекцию в JSON-файл.

        Параметры:
        filename (str): Имя файла для сохранения.
        """
        with open(filename, "w") as file:
            json.dump([s.to_dict() for s in self._data], file)

    def load(self, filename: str) -> None:
        """
        Загружает коллекцию из JSON-файла.

        Параметры:
        filename (str): Имя файла для загрузки.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self._data = [LineSegment.from_dict(s) for s in data]
        except FileNotFoundError:
            print("Файл не найден.")
