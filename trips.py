balik = []

def takebike(station, id):
    return station.btake(id)

def bytypetake(station, type):
    return station.btake_type(type)

def returnbike(client, bike, station, minutes):
    station.breturn(bike)
    cost = bike.countcost(minutes)
    if client.pay(cost):
        _revenue.append(cost)
        return cost
    return None

def summoney():
    return sum(balik)
