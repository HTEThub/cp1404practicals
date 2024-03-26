from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    read_guitars_csv(FILENAME, guitars)
    guitars.sort()
    for eachGuitar in guitars:
        print(eachGuitar)


def read_guitars_csv(filename, guitars):
    in_file = open(filename, 'r', newline='')
    for eachLine in in_file:
        split_line = eachLine.strip().split(',')
        guitar = Guitar(split_line[0], split_line[1], split_line[2])
        guitars.append(guitar)
    in_file.close()


main()
