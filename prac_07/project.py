import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    # Implement methods for sorting/comparing Project objects based on priority order
    def __lt__(self, other):
        return self.start_date < other.start_date

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate}, completion: {self.completion}%"


