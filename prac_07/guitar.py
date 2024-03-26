class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

        self.age = 0

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        self.age = 2024 - self.year

    def is_vintage(self):
        return self.age >= 50
