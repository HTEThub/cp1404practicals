from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    read_guitars_csv(FILENAME)


def read_guitars_csv(filename):
    guitars = []
    in_file = open(filename, 'r', newline='')
    for eachLine in in_file:
        split_line = eachLine.strip().split(',')
        guitars.append(str(Guitar(split_line[0], split_line[1], split_line[2])))
    in_file.close()

    print(guitars)





main()