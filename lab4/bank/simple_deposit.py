from deposit import Deposit

class SimpleDeposit(Deposit):
    """
    Класс срочного вклада с простыми процентами.
    """
    def calculate_profit(self) -> float:
        """
        Рассчитывает прибыль по формуле простых процентов.
        
        Результат:
        float: Прибыль по вкладу.
        """
        return self.amount * (self.rate / 100) * self.period