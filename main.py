from bike import Bike
from client import Client
from station import Station
from trips import take_bike, take_bike_by_type, return_bike, total_revenue


def build_report(stations):
    lines = ["=== Звіт адміністратора ==="]
    for s in stations:
        lines.append(f"Станція {s.name}: {s.count()} велосипедів")
    lines.append(f"Загальна виручка мережі: {total_revenue()} грн")
    return "\n".join(lines)


def ride(client, station_from, station_to, minutes, type):
    bike = take_bike_by_type(station_from, type)
    if bike is None:
        print(f"{client.name}: на станції {station_from.name} немає велосипедів типу {type}.")
        return
    cost = return_bike(client, bike, station_to, minutes)
    if cost is None:
        print(f"{client.name}: не вистачило грошей за поїздку на велосипеді №{bike.id}.")
    else:
        print(f"{client.name}: поїздка {minutes} хв на №{bike.id} ({type}), списано {cost} грн.")


def main():
    a = Station("A")
    b = Station("B")

    for bike in (Bike("normal", 1), Bike("normal", 2), Bike("electric", 3)):
        a.breturn(bike)
    for bike in (Bike("normal", 4), Bike("electric", 5)):
        b.breturn(bike)

    olya = Client("Оля", 200)
    petro = Client("Петро", 30)

    ride(olya, a, b, 20, "electric")
    ride(petro, b, a, 10, "normal")
    ride(olya, a, b, 15, "normal")

    ride(petro, a, b, 5, "electric")

    print(f"Баланс {olya.name}: {olya.balance} грн")
    print(f"Баланс {petro.name}: {petro.balance} грн")

    print(build_report([a, b]))


    assert a.count() + b.count() == 5
    assert total_revenue() == 150
    assert Bike("electric", 99).countcost(2) == 10
    assert take_bike(a, 12345) is None


if __name__ == "__main__":
    main()
