class Station:
    def __init__(self, name):
        self.name = name
        self.elist = []
        self.normlist = []

    def btake(self, id):
        for bikes in (self.elist, self.normlist):
            for bike in bikes:
                if bike.id == id:
                    bikes.remove(bike)
                    return bike
        return None

    def btake_type(self, type):
        bikes = self.elist if type == "electric" else self.normlist
        if bikes:
            return bikes.pop(0)
        return None

    def breturn(self, bike):
        if bike.type == "electric":
            self.elist.append(bike)
        else:
            self.normlist.append(bike)

    def count(self):
        return len(self.elist) + len(self.normlist)
