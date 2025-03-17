from simple_deposit import SimpleDeposit
from bonus_deposit import BonusDeposit
from capitalized_deposit import CapitalizedDeposit
from user import User
from bank import Bank

user = User("SAsha", 1000000)
bank = Bank("Bank")

simple_deposit = SimpleDeposit(5000, 5, 2)
bonus_deposit = BonusDeposit(10000, 5, 2, 7000, 10)
capitalized_deposit = CapitalizedDeposit(5000, 5, 2)

bank.add_deposit(simple_deposit)
bank.add_deposit(bonus_deposit)
bank.add_deposit(capitalized_deposit)

bank.show_deposits()
