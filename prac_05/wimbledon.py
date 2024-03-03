"""
Emails
Estimate: 50 minutes
Actual:  45 minutes

"""


FILENAME = "wimbledon.csv"
BREAK_LINE = "----------"


def main():
    countries_won = []
    champ_to_wins = {}
    countries_won, champ_to_wins = read_wimbleton_csv(FILENAME, countries_won, champ_to_wins)

    print("Wimbledon Champions:")
    display_champs_to_wins(champ_to_wins)

    print(BREAK_LINE)
    print(f"These {len(countries_won)} have won Wimbledon:")
    display_countries_won(countries_won)


def read_wimbleton_csv(filename, countries_won, champ_to_wins):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for eachLine in in_file:
            stripped_line = eachLine.strip()
            columns = stripped_line.split(",")

            if columns[1] not in countries_won:
                countries_won.append(columns[1])

            if columns[2] in champ_to_wins:
                champ_to_wins[columns[2]] += 1
            else:
                champ_to_wins[columns[2]] = 1

        countries_won.remove("Country")
        countries_won.sort()
        champ_to_wins.pop("Champion")
        return countries_won, champ_to_wins


def display_champs_to_wins(champ_to_wins):
    for champ, win in champ_to_wins.items():
        print(f"{champ} {win}")


def display_countries_won(countries_won):
    for i in range(0, len(countries_won)):
        if i == len(countries_won)-1:
            print(f"{countries_won[i]}", end="")
        else:
            print(f"{countries_won[i]}, ", end="")


main()




