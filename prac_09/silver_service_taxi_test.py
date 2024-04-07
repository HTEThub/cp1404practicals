from prac_09.silver_service_taxi import SilverServiceTaxi

my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
my_silver_taxi.drive(18)
print(my_silver_taxi.get_silver_fare())
print(my_silver_taxi)
my_silver_taxi.start_fare()
print(my_silver_taxi)
