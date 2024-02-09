min_chars = 5

characters = input("Enter anything: ")
while len(characters) != min_chars:
    print("Not enough characters")
    characters = input(str("Enter anything: "))
for eachChar in characters:
    print("*", end="")
