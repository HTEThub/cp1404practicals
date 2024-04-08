from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("LOL", 100, 50)
my_car.add_fuel(100)
distance = my_car.drive(50)
print(distance)
print(my_car)
