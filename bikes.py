PRICES = {"normal": 2, "electric": 5}

class Bike:
    def __init__(self, type, id):
        self.type = type
        self.id = id
        self.time = 0
    def get_p(self, type=None):
        return PRICES[type or self.type]
    def countcost(self, time):
        self.time = time
        return time * self.get_p(self.type)
