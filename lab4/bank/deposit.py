from abc import ABC, abstractmethod

class Deposit(ABC):
    """
    Абстрактный класс для банковских вкладов.
    """
    def __init__(self, amount: float, rate: float, period: int) -> None:
        """
        Инициализация вклада.
        
        Параметры:
        amount (float): Сумма вклада.
        rate (float): Годовая процентная ставка.
        period (int): Срок вклада в годах.
        """
        self.amount = amount
        self.rate = rate
        self.period = period
    
    @abstractmethod
    def calculate_profit(self) -> float:
        """
        Абстрактный метод расчета прибыли.
        
        Результат:
        float: Прибыль по вкладу.
        """
        pass