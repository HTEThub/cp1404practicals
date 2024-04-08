from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MAIN_MENU = "q)uit, c)hoose taxi, d)rive"
ENTER_HERE = ">>> "
LINE_BREAK = "----------"


def main():
    taxis_available = []
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis_available.append(prius)
    taxis_available.append(limo)
    taxis_available.append(hummer)

    current_taxi = None
    bill = 0.00
    print("Let's drive!")
    print(MAIN_MENU)
    choice = input(ENTER_HERE).lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis_available)
        elif choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                bill = drive(current_taxi, bill)
        else:
            print("Invalid Input")
        print(f"Bill to date: {bill:.2f}")
        print(LINE_BREAK)
        print(MAIN_MENU)
        choice = input(ENTER_HERE).lower()
    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis_available):
        print(f"{i} - {taxi}")


def choose_taxi(taxis_available):
    print("Taxi/s available:")
    for i, taxi in enumerate(taxis_available):
        print(f"{i} - {taxi}")
    while True:
        try:
            choice = int(input(ENTER_HERE))
            var = taxis_available[choice]
            break
        except ValueError:
            print("Invalid input. Choose a number from the list")
        except IndexError:
            print("Out of range. Choose a number from the list")
    return taxis_available[choice]


def drive(current_taxi, bill):
    if current_taxi.fuel == 0:
        print(f"There's no more fuel in {current_taxi.car_name}!")
    else:
        current_taxi.start_fare()
        while True:
            try:
                distance = int(input("Drive how far? "))
                while distance < 0:
                    print("Cannot be less than 0")
                    distance = int(input("Drive how far? "))
                break
            except ValueError:
                print("Invalid input. Enter whole number")
        current_taxi.drive(distance)

        price = current_taxi.get_fare()
        print(f"Your {current_taxi.car_name} trip cost you ${price:.2f}")

        bill += price
    return bill


main()
