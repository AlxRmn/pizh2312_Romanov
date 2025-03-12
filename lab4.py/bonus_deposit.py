from deposit import Deposit

class BonusDeposit(Deposit):
    """
    Класс бонусного вклада.
    """
    def __init__(self, amount: float, rate: float, period: int, bonus_threshold: float, bonus_percentage: float) -> None:
        """
        Инициализация бонусного вклада.
        
        Параметры:
        amount (float): Сумма вклада.
        rate (float): Годовая процентная ставка.
        period (int): Срок вклада в годах.
        bonus_threshold (float): Минимальная сумма для начисления бонуса.
        bonus_percentage (float): Процент бонуса от прибыли.
        """
        super().__init__(amount, rate, period)
        self.bonus_threshold = bonus_threshold
        self.bonus_percentage = bonus_percentage
    
    def calculate_profit(self) -> float:
        """
        Рассчитывает прибыль с учетом бонуса.
        
        Результат:
        float: Итоговая прибыль.
        """
        profit = self.amount * (self.rate / 100) * self.period
        if self.amount > self.bonus_threshold:
            profit += profit * (self.bonus_percentage / 100)
        return profit