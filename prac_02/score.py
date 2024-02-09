import random


def main():
    EXCELLENCE_THRESHOLD = 90
    PASS_THRESHOLD = 50
    MAX_SCORE = 100
    MIN_SCORE = 0

    score = get_validated_score(MAX_SCORE, MIN_SCORE)

    grades = get_grades(EXCELLENCE_THRESHOLD, PASS_THRESHOLD, score)

    print(grades)

    print("Random Score:", random.randint(1, 100))


def get_validated_score(MAX_SCORE, MIN_SCORE):
    """ Get score input and check if it's valid """
    score = float(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid Input")
        score = float(input("Enter score: "))
    return score


def get_grades(EXCELLENCE_THRESHOLD, PASS_THRESHOLD, score):
    """ Grading the scores using threshold """
    if score > EXCELLENCE_THRESHOLD:
        return "Excellence"
    elif score >= PASS_THRESHOLD:
        return "Pass"
    else:
        return "Fail"


main()
