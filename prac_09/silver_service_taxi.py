from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        normal_price = Taxi.price_per_km
        self.price_per_km = normal_price * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_silver_fare(self):
        if super().get_fare() != 0:
            return super().get_fare() + self.flagfall
        else:
            return super().get_fare()
