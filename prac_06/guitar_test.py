from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 2000, 100)
print(f"Gibson expected 24. Got {gibson.get_age()}")
print(f"Gibson expected False. Got {gibson.is_vintage()}")

another_guitar = Guitar("Another guitar", 1900, 110)
print(f"Another guitar expected 124. Got {another_guitar.get_age()}")
print(f"Another guitar expected True. Got {another_guitar.is_vintage()}")


