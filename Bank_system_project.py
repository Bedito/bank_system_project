import random
import asyncio


def log_islem(func):
    def wrapper(*args, **kwargs):
        print("İşlem Başlatıldı...")
        result = func(*args, **kwargs)
        print("İşlem bitti...")
        return result

    return wrapper


class BankAccount:
    def __init__(self, user_name: str, password: int, balance: int) -> None:
        self.__user = user_name
        self.__password = password
        self.balance = balance
        self.__bank_account = random.randint(1_000_000_000, 9_999_999_999)
        self.gecmis = []

    def gecmis_goster(self):
        for i in self.gecmis:
            yield i

    async def para_transferi(self,hedef_hesap, miktar):
        if self.balance < miktar:
            raise ValueError("Yetersiz Bakiye")
        print("Transfer Başladı..")
        await asyncio.sleep(2)
        self.balance -= miktar
        hedef_hesap.balance += miktar
        print("Transfer tamamlandı...")



    @log_islem
    def deposit(self, amount: int):
        self.balance += amount
        print(self.balance)
        self.gecmis.append({"islem": "deposit", "miktar": amount, "bakiye": self.balance})

    @log_islem
    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError(f"Your balance is not enough.{self.balance}")
        self.balance -= amount
        self.gecmis.append({"islem": "withdraw", "miktar": amount, "bakiye": self.balance})

    def show_the_balance(self):
        print(self.balance)

class DepositAccount(BankAccount):
    def __init__(self,user_name, password, balance, vade, faiz):
        super().__init__(user_name, password, balance)
        self.vade = vade
        self.faiz = faiz

    def faiz_hesaplama(self):
        new_balance = self.balance * (1 + self.faiz/100) * self.vade
        self.balance = new_balance
        return self.balance

    def show_the_balance(self):
        return self.balance, self.vade, self.faiz



account = BankAccount("Bedirhan", 1234, 5000)
account2 = BankAccount("Bilo", 1356, 4000)
account.deposit(500)
account.deposit(1500)
asyncio.run(account.para_transferi(account2, 1000))
account2.show_the_balance()
for islem in account.gecmis_goster():
    print(islem)







