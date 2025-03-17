from deposit import Deposit

class CapitalizedDeposit(Deposit):
    """
    Класс вклада с капитализацией процентов.
    """
    def calculate_profit(self) -> float:
        """
        Рассчитывает прибыль по формуле сложных процентов.
        
        Результат:
        float: Итоговая прибыль.
        """
        return self.amount * ((1 + self.rate / 100) ** self.period - 1)