from deposit import Deposit

class Bank:
    """
    Класс банка, управляющего вкладами.
    """
    def __init__(self, name: str) -> None:
        """
        Инициализация банка.
        
        Параметры:
        name (str): Название банка.
        """
        self.name = name
        self.deposits = []
    
    def add_deposit(self, deposit: Deposit) -> None:
        """
        Добавляет вклад в банк.
        
        Параметры:
        deposit (Deposit): Вклад, который добавляется.
        """
        self.deposits.append(deposit)
    
    def show_deposits(self) -> None:
        """
        Выводит информацию о вкладах в банке.
        """
        for deposit in self.deposits:
            print(f"Deposit Type: {deposit.__class__.__name__}, Profit: {deposit.calculate_profit():.2f}")
