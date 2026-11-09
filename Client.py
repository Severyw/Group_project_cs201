class Client:
    def __init__(self, name, balance:int):
        self.name = name
        self.balance = balance

    def can_pay(self, price):         # перевірка чи достатньо балансу
        if_can_pay = self.balance >= price
        return if_can_pay

    def pay(self, price):            # Плата за поїздку
        self.balance -= price

if __name__ == "__main__":
    name = Client("John", 100)
    paid = name.can_pay(500)
    if paid:
        print("Payment successful")
        name.pay(500)
    else:
        print("Insufficient funds")

    print(name.balance)

