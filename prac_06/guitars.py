from prac_06.guitar import Guitar

guitars = []

guitar_name = input("Name: ")
while guitar_name.strip() != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))

    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

    the_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    print(f"{the_guitar} added.")

    print()
    guitar_name = input("Name: ")

print("\n... snip ...\n")

for i, eachGuitar in enumerate(guitars, 1):
    eachGuitar.get_age()
    if eachGuitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""

    print(f"Guitar {i}: {eachGuitar.name:>20} ({eachGuitar.year}), worth ${eachGuitar.cost:>10,.2f} {vintage_string}")
