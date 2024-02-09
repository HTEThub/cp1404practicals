def main():
    MIN_CHARS = 5
    password = get_password(MIN_CHARS)
    print_stars(password)


def print_stars(password):
    for each_char in password:
        print("*", end="")


def get_password(MIN_CHARS):
    password = input("Enter anything: ")
    while len(password) != MIN_CHARS:
        print("Not enough characters")
        password = input(str("Enter anything: "))
    return password


main()