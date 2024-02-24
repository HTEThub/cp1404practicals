import random

MIN_NUM = 1
MAX_NUM = 45
MAX_RANDOM_NUM_COUNT = 6


num_of_picks = int(input("How many quick picks?: "))
for eachPick in range(num_of_picks):
    random_numbers = []

    for eachNumber in range(MAX_RANDOM_NUM_COUNT):
        random_number = random.randint(MIN_NUM, MAX_NUM)
        while random_number in random_numbers:
            random_number = random.randint(MIN_NUM, MAX_NUM)
        random_numbers.append(random_number)

    random_numbers.sort()

    for eachElement in random_numbers:
        print(f"{eachElement:2}", end=" ")
    print()
