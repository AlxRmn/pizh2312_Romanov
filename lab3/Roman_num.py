class Number:
    def __init__(self, value: int):
        self._value = value
    
    def get_value(self) -> int:
        return self._value


class Roman(Number):
    __roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    __int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    def __init__(self, value: str | int):
        if isinstance(value, str):
            super().__init__(self.__roman_to_int(value))
            self.__roman = value
        elif isinstance(value, int):
            super().__init__(value)
            self.__roman = self.__int_to_roman(value)
    
    def get_roman(self) -> str:
        return self.__roman
    
    @staticmethod
    def __roman_to_int(roman: str) -> int:
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
        result = []
        for (arabic, roman) in Roman.__int_to_roman_map:
            while number >= arabic:
                result.append(roman)
                number -= arabic
        return ''.join(result)
    
    def __add__(self, other: Number) -> 'Roman':
        if isinstance(other, Roman):
            return Roman(self.get_value() + other.get_value())
        elif isinstance(other, int):
            return Roman(self.get_value() + other)
    
    def __sub__(self, other: Number | int) -> 'Roman':
        if isinstance(other, Roman):
            return Roman(self.get_value() - other.get_value())
        elif isinstance(other, int):
            return Roman(self.get_value() - other)
    
    def __mul__(self, other: Number | int) -> 'Roman':
        if isinstance(other, Roman):
            return Roman(self.get_value() * other.get_value())
        elif isinstance(other, int):
            return Roman(self.get_value() * other)
        
    def __truediv__(self, other: Number | int) -> 'Roman':
        if isinstance(other, Roman):
            return Roman(self.get_value() // other.get_value())
        elif isinstance(other, int):
            return Roman(self.get_value() // other)
    
    def __str__(self) -> str:
        return f"{self.get_roman()} ({self.get_value()})"


# Пример использования
a = Roman("X")
b = Roman(5)

print(a)  # X (10)
print(b)  # V (5)

# Операции
print(a + b)  # XV (15)
print(a - b)  # V (5)
print(a * 2)  # XX (20)
print(a / b)  # II (2)
