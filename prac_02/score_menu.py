def main():
    EXCELLENCE_THRESHOLD = 90
    PASS_THRESHOLD = 50
    MAX_SCORE = 100
    MIN_SCORE = 0
    score = 0

    MENU = "(G)et a valid score\n" \
           "(P)rint result\n" \
           "(S)how stars\n" \
           "(Q)uit\n"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(MAX_SCORE, MIN_SCORE)
        elif choice == "P":
            result = print_result(score, EXCELLENCE_THRESHOLD, PASS_THRESHOLD)
            print("Your Score:", score)
            print("Result:", result)
        elif choice == "S":
            print("Here's how many stars you get for the score:", score)
            show_stars(score)
        else:
            print("Invalid Choice")

        print()
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score(MAX_SCORE, MIN_SCORE):
    score = int(input("Enter a Valid score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("That's an Invalid score!")
        score = int(input("Enter a Valid score: "))
    return score


def print_result(score, EXCELLENCE_THRESHOLD, PASS_THRESHOLD):
    if score > EXCELLENCE_THRESHOLD:
        return "Excellence!"
    elif score > PASS_THRESHOLD:
        return "Pass."
    else:
        return "Fail!"


def show_stars(score):
    """ Count and print as many stars as the score """
    for i in range(score):
        print("*", end="")
    print()  # for skipping a line


main()
