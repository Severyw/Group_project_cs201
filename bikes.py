prices = {"normal": 2, "electric": 5}

class Bike:
    def __init__(self, type, id, time = 0):
        self.type = type
        self.id = id
        self.time = time
    def get_p(self, type):
        if type == "electric":
            return 5
        return 2
    def countcost(self, time):
        self.time = time
        return time * self.get_p(self.type)
