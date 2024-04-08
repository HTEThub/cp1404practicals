from prac_09.silver_service_taxi import SilverServiceTaxi

my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(my_silver_taxi.get_silver_fare())
print(my_silver_taxi)

my_silver_taxi.drive(18)
print(my_silver_taxi.get_silver_fare())
print(my_silver_taxi)

my_silver_taxi.start_fare()
print(my_silver_taxi.get_silver_fare())
print(my_silver_taxi)

my_silver_taxi.drive(200)
print(f"{my_silver_taxi.get_silver_fare():.2f}")
print(my_silver_taxi)
