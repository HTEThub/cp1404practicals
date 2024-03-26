COLOUR_TO_CODE = {"absolute_zero": "#0048ba", "acid_green": "#b0bf1a", "alice_blue": "#f0f8ff",
                  "alizarin_crimson": "#e32636", "amber": "#ffbf00", "amethyst": "#9966cc", "aqua": "#00ffff",
                  "ash_grey": "#b2beb5", "asparagus": "#87a96b", "aureolin": "#fdee00"}
for eachKey in COLOUR_TO_CODE:
    print(eachKey)
print("----------")
picked_colour = input("Enter one of the listed colours: ").lower()
while picked_colour != "":
    try:
        print(f"{picked_colour} is {COLOUR_TO_CODE[picked_colour]}")
    except KeyError:
        print("Invalid input")
    print("----------")
    picked_colour = input("Enter one of the listed colours: ").lower()
