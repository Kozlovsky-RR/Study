"""Система для управления банковскими счетамим."""
class BankAccount:
    def __init__(self, number: str, name: str, balance: int) -> None:
        self.number = number
        self.name = name

        if isinstance(balance, int) and balance >= 0:
            self.balance = balance
        else:
            raise TypeError("Баланс должен быть положительным числом")

    def deposit(self, value: int) -> None:
        """Депозит средств."""
        if value > 0:
            self.balance += value

    def withdraw(self, value: int) -> bool:
        """Снятие средств со счета."""
        if value > 0 and self.balance - value >= 0:
            self.balance -= value
            return True
        else:
            print("Снятие средств невозможно")
            return False

    def check_balance(self) -> int:
        return self.balance

    def __str__(self) -> str:
        return f"Номер счета: {self.number}; Имя владельца: {self.name}; Баланс: {self.balance}"

    def __repr__(self) -> str:
        return (f"BankAccount(number='{self.number}'), BankAccount(name='{self.name}'),"
                f" BankAccount(balance='{self.balance}')")

    def __eq__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.number == other.number and self.name == other.name
        return NotImplemented

    def __iter__(self) -> tuple:
        yield from (self.number, self.name, self.balance)


class BankSystem:
    def __init__(self) -> None:
        self.accounts = dict()

    def add_account(self, account: BankAccount) -> None:
        self.accounts[account.number] = account

    def transfer(self, number1: str, number2: str, value: int) -> None:
        """Перевод стредств с одного счета на другой."""
        for v in self.accounts.values():
            if number1 in v:
                if v.withdraw(value) is False:
                    print("Превышен лимит средств")
                    break
            elif number2 in v:
                v.deposit(value)
            else:
                print("Неверно указан один из номеров счета")


account1 = BankAccount("12345", "Иван Иванов", 1000)
account2 = BankAccount("67890", "Петр Петров", 2000)
bank = BankSystem()
bank.add_account(account1)
bank.add_account(account2)
print(account1)
account1.deposit(200)
print(account1)
account1.withdraw(100)
print(account1.check_balance())
print(account1 != account2)
print(bank.accounts)
bank.transfer("12345", "67890", 1098)
print(bank.accounts)