# 1.
NAMES_FILE = "names_list.txt"

name = input("Enter your name: ")
out_file = open(NAMES_FILE, "w")
print(name, file=out_file)
out_file.close()


# 2.
in_file = open(NAMES_FILE, "r")
for eachLine in in_file:
    print(f"Your name is {eachLine}")
in_file.close()


# 3.
NUMBERS_FILE = "numbers.txt"
total = 0

in_file = open(NUMBERS_FILE, "r")
text = in_file.readlines()
for eachLine in range(0, len(text)-1):
    number = int(text[eachLine])
    total += number
print(total)
in_file.close()


# 4.
total_2 = 0
in_file = open(NUMBERS_FILE, "r")
text = in_file.readlines()
for eachLine in range(0, len(text)):
    number = int(text[eachLine])
    total_2 += number
print(total_2)
in_file.close()
