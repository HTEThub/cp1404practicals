from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    read_guitars_csv(FILENAME, guitars)
    guitars.sort()
    for eachGuitar in guitars:
        print(eachGuitar)

    print()
    get_guitars(guitars)
    guitars.sort()
    write_guitars_csv(FILENAME, guitars)


def get_guitars(guitars):
    guitar_brand = input("Enter Brand: ")
    while guitar_brand.strip() != "":
        guitar_year = error_checking_year("Enter Year: ")
        guitar_cost = error_checking_cost("Enter Cost: ")
        guitar = Guitar(guitar_brand, guitar_year, guitar_cost)
        guitars.append(guitar)

        print(f"{guitar_brand} ({guitar_year}): ${guitar_cost} added")

        guitar_brand = input("Enter brand: ")


def read_guitars_csv(filename, guitars):
    in_file = open(filename, 'r', newline='')
    for eachLine in in_file:
        split_line = eachLine.strip().split(',')
        guitar = Guitar(split_line[0], int(split_line[1]), split_line[2])
        guitars.append(guitar)
    in_file.close()


def write_guitars_csv(filename, guitars):
    out_file = open(filename, 'w', newline='')
    for eachGuitar in guitars:
        out_file.write(f"{eachGuitar.brand},{eachGuitar.year},{eachGuitar.cost}\n")
    out_file.close()


def error_checking_year(input_prompt):
    while True:
        try:
            year = int(input(input_prompt))
            while year < 0:
                print("Cannot be less than 0")
                year = int(input(input_prompt))
            break
        except ValueError:
            print("Can only be full numbers")
    return year


def error_checking_cost(input_prompt):
    while True:
        try:
            cost = float(input(input_prompt))
            while cost < 0:
                print("Cannot be less than 0")
                cost = float(input(input_prompt))
            break
        except ValueError:
            print("Can only be numbers")
    return cost


main()
