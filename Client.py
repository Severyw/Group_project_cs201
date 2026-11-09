class Client:
    def __init__(self, name, balance:int):
        self.name = name
        self.balance = balance

    def can_pay(self, price):         # перевірка чи достатньо балансу
        return self.balance >= price

    def pay(self, price):            # Плата за поїздку
        if not self.can_pay(price):
            return False
        self.balance -= price
        return True



