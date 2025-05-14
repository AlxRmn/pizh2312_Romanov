class Number:
    """
    Описание:
    Базовый класс для работы с числами.
    Этот класс предназначен для хранения целочисленных значений и получения их.
    """
    
    def __init__(self, value: int):
        """
        Назначение:
        Инициализирует объект с переданным значением числа.
        
        Параметры:
        value (int): Арабское число, которое будет сохранено в объекте.
        
        Результат:
        Экземпляр класса Number с инициализированным значением.
        """
        self._value = value
    
    def get_value(self) -> int:
        """
        Назначение:
        Получить арабское значение числа.
        
        Параметры:
        None
        
        Результат:
        int: Арабское число, которое хранится в объекте.
        """
        return self._value


class Roman(Number):
    """
    Описание:
    Класс для работы с римскими числами. Этот класс позволяет преобразовывать римские числа в арабские и наоборот,
    а также выполнять арифметические операции (+, -, *, /) с римскими и арабскими числами.
    """
    
    __roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    __int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    def __init__(self, value):
        """
        Назначение:
        Инициализирует объект римского числа, преобразуя строку или арабское число в римское представление.
        
        Параметры:
        value: Римское число в виде строки или арабское число в виде целого числа.
        
        Результат:
        Экземпляр класса Roman с римским и арабским значением.
        """
        if type(value) == str:
            super().__init__(self.__roman_to_int(value))
            self.__roman = value
        elif type(value) == int:
            super().__init__(value)
            self.__roman = Roman.__int_to_roman(value)
    
    def get_roman(self) -> str:
        """
        Назначение:
        Получить римское представление числа.
        
        Параметры:
        None
        
        Результат:
        str: Римское число, соответствующее текущему арабскому значению.
        """
        return self.__roman
    
    @staticmethod
    def __roman_to_int(roman: str) -> int:
        """
        Назначение:
        Преобразует римское число в арабское.
        
        Параметры:
        roman (str): Римское число в виде строки.
        
        Результат:
        int: Арабское число, соответствующее римскому числу.
        """
        result = 0
        prev_value = 0
        for char in reversed(roman):
            value = Roman.__roman_to_int_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result
    
    @staticmethod
    def __int_to_roman(number: int) -> str:
        """
        Назначение:
        Преобразует арабское число в римское.
        
        Параметры:
        number (int): Арабское число, которое необходимо преобразовать.
        
        Результат:
        str: Римское число, соответствующее арабскому числу.
        """
        result = []
        for arabic, roman in Roman.__int_to_roman_map:
            count = number // arabic  
            result.append(roman * count)  
            number -= arabic * count  
        return ''.join(result)
    
    def __add__(self, other) -> 'Roman':
        """
        Назначение:
        Выполняет сложение двух чисел (римских или арабских).
        
        Параметры:
        other (Roman | int): Второе число для сложения (римское число или арабское число).
        
        Результат:
        Roman: Новый объект Roman, который представляет результат сложения.
        """
        if type(other) == Roman:
            return Roman(self.get_value() + other.get_value())
        elif type(other) == int:
            return Roman(self.get_value() + other)
    
    def __sub__(self, other) -> 'Roman':
        """
        Назначение:
        Выполняет вычитание двух чисел (римских или арабских).
        
        Параметры:
        other (Roman | int): Второе число для вычитания (римское число или арабское число).
        
        Результат:
        Roman: Новый объект Roman, который представляет результат вычитания.
        """
        if type(other) == Roman:
            return Roman(self.get_value() - other.get_value())
        elif type(other) == int:
            return Roman(self.get_value() - other)
    
    def __mul__(self, other) -> 'Roman':
        """
        Назначение:
        Выполняет умножение двух чисел (римских или арабских).
        
        Параметры:
        other (Roman | int): Второе число для умножения (римское число или арабское число).
        
        Результат:
        Roman: Новый объект Roman, который представляет результат умножения.
        """
        if type(other) == Roman:
            return Roman(self.get_value() * other.get_value())
        elif type(other) == int:
            return Roman(self.get_value() * other)
    
    def __truediv__(self, other) -> 'Roman':
        """
        Назначение:
        Выполняет деление двух чисел (римских или арабских).
        
        Параметры:
        other (Roman | int): Второе число для деления (римское число или арабское число).
        
        Результат:
        Roman: Новый объект Roman, который представляет результат деления (целочисленное).
        """
        if type(other) == Roman:
            return Roman(self.get_value() // other.get_value())
        elif type(other) == int:
            return Roman(self.get_value() // other)
    
    def __str__(self) -> str:
        """
        Назначение:
        Возвращает строковое представление объекта Roman.
        
        Параметры:
        None
        
        Результат:
        str: Строковое представление числа в римской и арабской формах.
        """
        return f"{self.get_roman()} ({self.get_value()})"


class RomanArithmetic:
    """
    Описание:
    Класс для выполнения арифметических операций с римскими числами.
    Этот класс позволяет выполнять основные арифметические операции между объектами Roman.
    """
    
    @staticmethod
    def add(a: Roman, b: Roman) -> Roman:
        """
        Назначение:
        Выполняет сложение двух римских чисел.
        
        Параметры:
        a (Roman): Первое римское число.
        b (Roman): Второе римское число.
        
        Результат:
        Roman: Результат сложения.
        """
        return Roman(a.get_value() + b.get_value())
    
    @staticmethod
    def subtract(a: Roman, b: Roman) -> Roman:
        """
        Назначение:
        Выполняет вычитание двух римских чисел.
        
        Параметры:
        a (Roman): Первое римское число.
        b (Roman): Второе римское число.
        
        Результат:
        Roman: Результат вычитания.
        """
        return Roman(a.get_value() - b.get_value())
    
    @staticmethod
    def multiply(a: Roman, b: Roman) -> Roman:
        """
        Назначение:
        Выполняет умножение двух римских чисел.
        
        Параметры:
        a (Roman): Первое римское число.
        b (Roman): Второе римское число.
        
        Результат:
        Roman: Результат умножения.
        """
        return Roman(a.get_value() * b.get_value())
    
    @staticmethod
    def divide(a: Roman, b: Roman) -> Roman:
        """
        Назначение:
        Выполняет деление двух римских чисел.
        
        Параметры:
        a (Roman): Первое римское число.
        b (Roman): Второе римское число.
        
        Результат:
        Roman: Результат деления.
        """
        return Roman(a.get_value() // b.get_value())


# Пример использования
a = Roman("X")
b = Roman(5)

print(f"Сложение: {RomanArithmetic.add(a, b)}")  # XV (15)
print(f"Вычитание: {RomanArithmetic.subtract(a, b)}")  # V (5)
print(f"Умножение: {RomanArithmetic.multiply(a, b)}")  # XX (20)
print(f"Деление: {RomanArithmetic.divide(a, b)}")  # II (2)
