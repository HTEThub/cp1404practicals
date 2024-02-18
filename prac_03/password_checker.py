"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password, SPECIAL_CHARACTERS, MIN_LENGTH, MAX_LENGTH):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password, special_characters, min_length, max_length):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if max_length > len(password) < min_length:
        print(f"There are: {len(password)} character/s. "
              f"There should be between {min_length} and {max_length} character/s")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if char in special_characters:
            count_special += 1
    print(f"There are: {count_lower} lower/s, {count_upper} upper/s, "
          f"{count_digit} digit/s and {count_special} special/s")

    # TODO: if any of the 'normal' counts are zero, return False
    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
