class User:
    """
    Класс пользователя банка.
    """
    def __init__(self, name: str, balance: float) -> None:
        """
        Инициализация пользователя.
        
        Параметры:
        name (str): Имя пользователя.
        balance (float): Баланс пользователя.
        """
        self.name = name
        self.balance = balance
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление пользователя.
        
        Результат:
        str: Информация о пользователе.
        """
        return f"User: {self.name}, Balance: {self.balance}"